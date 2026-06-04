#!/usr/bin/env bash
set -euo pipefail

log() { echo "[init-db] $*"; }
need() { command -v "$1" >/dev/null 2>&1 || { echo "[init-db] Missing: $1" >&2; exit 1; }; }

# --- macOS (Homebrew) MariaDB init script ---
# - Installs MariaDB via Homebrew
# - Starts mariadbd manually with --no-defaults (ignores my.cnf)
# - Initialises datadir if needed
# - Creates DB 'school' and user 'student' (password: studentpw)
# - Optionally seeds from /tmp/seed.sql

need brew

log "Installing MariaDB (if needed)…"
brew install mariadb >/dev/null 2>&1 || true

need mariadbd
need mariadb-install-db
need mysqladmin
need mariadb

DATA_DIR="$(brew --prefix)/var/mysql"
LOG_FILE="/tmp/mariadb.log"
PID_FILE="/tmp/mariadb.pid"
SOCK_FILE="/tmp/mariadb.sock"
HOST="127.0.0.1"
PORT="3306"

# Optional root password (set this in your shell before running if you want root provisioning)
# export MARIADB_ROOT_PASSWORD="rootpw"
ROOT_PW="${MARIADB_ROOT_PASSWORD:-}"

log "Preparing data dir…"
mkdir -p "$DATA_DIR"

# Initialise if system tables missing
if [[ ! -d "$DATA_DIR/mysql" ]]; then
  log "Initialising data directory at $DATA_DIR…"
  rm -rf "$DATA_DIR"/* 2>/dev/null || true
  mariadb-install-db --datadir="$DATA_DIR" >/dev/null
fi

log "Stopping any previous MariaDB processes…"
pkill -f mariadbd 2>/dev/null || true
pkill -f mysqld 2>/dev/null || true

log "Starting MariaDB (manual, ignoring config files)…"
nohup mariadbd \
  --no-defaults \
  --datadir="$DATA_DIR" \
  --bind-address="$HOST" \
  --port="$PORT" \
  --socket="$SOCK_FILE" \
  --pid-file="$PID_FILE" \
  --log-error="$LOG_FILE" \
  >/dev/null 2>&1 &

log -n "Waiting for MariaDB"
READY="false"
for _ in {1..60}; do
  if mysqladmin --no-defaults --protocol=TCP -h "$HOST" -P "$PORT" -u root ping --silent >/dev/null 2>&1; then
    READY="true"
    echo " ✓"
    break
  fi
  echo -n "."
  sleep 1
done

if [[ "$READY" != "true" ]]; then
  echo
  echo "[init-db] MariaDB did not become ready. Tail of log:" >&2
  tail -n 200 "$LOG_FILE" >&2 || true
  exit 1
fi

# If root password is set, use it. Otherwise attempt root passwordless.
ROOT_AUTH_ARGS=(--no-defaults --protocol=TCP -h "$HOST" -P "$PORT" -u root)
if [[ -n "$ROOT_PW" ]]; then
  ROOT_AUTH_ARGS+=("-p$ROOT_PW")
fi

log "Creating DB and accounts…"
mariadb "${ROOT_AUTH_ARGS[@]}" <<'SQL'
CREATE DATABASE IF NOT EXISTS school;

CREATE USER IF NOT EXISTS 'student'@'localhost' IDENTIFIED BY 'studentpw';
CREATE USER IF NOT EXISTS 'student'@'127.0.0.1' IDENTIFIED BY 'studentpw';
CREATE USER IF NOT EXISTS 'student'@'%' IDENTIFIED BY 'studentpw';

ALTER USER 'student'@'localhost' IDENTIFIED BY 'studentpw';
ALTER USER 'student'@'127.0.0.1' IDENTIFIED BY 'studentpw';
ALTER USER 'student'@'%' IDENTIFIED BY 'studentpw';

GRANT ALL PRIVILEGES ON *.* TO 'student'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'student'@'127.0.0.1';
GRANT ALL PRIVILEGES ON *.* TO 'student'@'%';
FLUSH PRIVILEGES;
SQL

# Optional seed
if [[ -f /tmp/seed.sql ]]; then
  log "Seeding school from /tmp/seed.sql…"
  mariadb --no-defaults --protocol=TCP -h "$HOST" -P "$PORT" -ustudent -pstudentpw school < /tmp/seed.sql || true
fi

log "Done."
log "Connect as student:"
log "  mariadb --no-defaults --protocol=TCP -h $HOST -P $PORT -ustudent -pstudentpw school"
