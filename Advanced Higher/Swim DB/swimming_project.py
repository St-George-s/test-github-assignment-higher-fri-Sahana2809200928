import mysql.connector
from dataclasses import dataclass
from typing import List, Optional

# -------------------------------
# Database configuration
# -------------------------------
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "student",
    "password": "studentpw",
    "database": "project1",
    "port": 3306
}

# -------------------------------
# Record structure (array of records)
# -------------------------------
@dataclass
class Swimmer:
    swimmer_id: int
    first_name: str
    last_name: str
    squad: str
    stroke_pref: Optional[str]
    personal_best_50_free_seconds: Optional[float]

# -------------------------------
# Database helpers
# -------------------------------
def open_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    return conn, cur

def close_db(conn, cur):
    cur.close()
    conn.close()

# -------------------------------
# Menu + input validation
# -------------------------------
def show_menu():
    print("\n--- Swimmers Menu ---")
    print("1. View swimmers by squad (custom messages)")
    print("2. Export all swimmers to file")
    print("3. Exit")

def get_menu_choice():
    while True:
        choice = input("Select an option (1-3): ").strip()
        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid choice. Please enter 1, 2 or 3.")

def get_squad():
    while True:
        squad = input("Enter squad (e.g. Lane 1): ").strip()
        if 1 <= len(squad) <= 50:
            return squad
        print("Invalid squad name.")

# -------------------------------
# Display helpers
# -------------------------------
def display_rows(cur):
    cols = [d[0] for d in cur.description] if cur.description else []
    if cols:
        print(" | ".join(cols))
        print("-" * len(" | ".join(cols)))
    for row in cur.fetchall():
        print(" | ".join(str(x) for x in row))

# -------------------------------
# Queries + logic
# -------------------------------
def print_custom_messages_for_squad(cur, squad):
    sql = """
    SELECT first_name, last_name, squad, personal_best_50_free_seconds
    FROM Swimmers
    WHERE squad = %s
    ORDER BY personal_best_50_free_seconds ASC
    """
    cur.execute(sql, (squad,))
    rows = cur.fetchall()

    if not rows:
        print(f"No swimmers found in {squad}.")
        return

    for first_name, last_name, squad_name, pb in rows:
        if pb is None:
            print(f"{first_name} {last_name} is in {squad_name}. No 50m freestyle PB recorded yet.")
        elif pb < 35:
            print(f"{first_name} {last_name} is flying in {squad_name}, PB = {pb:.2f}s. Excellent pace.")
        else:
            print(f"{first_name} {last_name} is in {squad_name}, PB = {pb:.2f}s. Keep pushing for a new best.")

def load_swimmers(cur) -> List[Swimmer]:
    sql = """
    SELECT swimmer_id,
           first_name,
           last_name,
           squad,
           stroke_pref,
           personal_best_50_free_seconds
    FROM Swimmers
    ORDER BY swimmer_id ASC
    """
    cur.execute(sql)
    swimmers: List[Swimmer] = []
    for row in cur.fetchall():
        swimmers.append(Swimmer(*row))
    return swimmers

def write_swimmers_to_file(swimmers: List[Swimmer], filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Swimmers Report\n")
        f.write("================\n\n")

        for s in swimmers:
            pb_text = "N/A" if s.personal_best_50_free_seconds is None else f"{s.personal_best_50_free_seconds:.2f}s"
            stroke_text = "N/A" if s.stroke_pref is None else s.stroke_pref

            f.write(f"ID: {s.swimmer_id}\n")
            f.write(f"Name: {s.first_name} {s.last_name}\n")
            f.write(f"Squad: {s.squad}\n")
            f.write(f"Stroke preference: {stroke_text}\n")
            f.write(f"50m Freestyle PB: {pb_text}\n")
            f.write("---\n")

# -------------------------------
# Main program
# -------------------------------
def main():
    conn, cur = open_db()
    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == "1":
                squad = get_squad()
                print_custom_messages_for_squad(cur, squad)

            elif choice == "2":
                swimmers = load_swimmers(cur)
                write_swimmers_to_file(swimmers, "swimmers_report.txt")
                print("Swimmers exported to swimmers_report.txt")

            elif choice == "3":
                print("Goodbye.")
                break

    finally:
        close_db(conn, cur)

if __name__ == "__main__":
    main()
