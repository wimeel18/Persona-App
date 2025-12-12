import sqlite3

conn = sqlite3.connect("C:/Users/Karin Sihotang/Documents/PersonaQuest.db")
c = conn.cursor()
c.execute("SELECT id, username, email FROM member")
rows = c.fetchall()
for r in rows:
    print(r)
conn.close()