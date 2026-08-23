import mysql.connector

# (1) OPEN CONNECTION
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="student",
    password="studentpw",
    database="project1",
    port=3306
)

cur = conn.cursor()

# (2) EXECUTE INSERT QUERY
cur.execute("""
INSERT INTO Swimmers 
(first_name, last_name, squad, stroke_pref, personal_best_50_free_seconds)
VALUES (%s, %s, %s, %s, %s)
""", ("Grace", "Hopper", "Lane 5", "Freestyle", 32.45))

conn.commit()

# (3) DISPLAY RESULTS
cur.execute("""
SELECT 
    swimmer_id,
    first_name,
    last_name,
    squad,
    stroke_pref,
    personal_best_50_free_seconds
FROM Swimmers
ORDER BY swimmer_id
""")

cols = [d[0] for d in cur.description]
print(" | ".join(cols))

for row in cur.fetchall():
    print(" | ".join(str(x) for x in row))

# (4) CLOSE CONNECTION
cur.close()
conn.close()