import sqlite3

class MiniTask:
    def __init__(self, id, title, priority):
        self.id = id
        self.title = title
        self.priority = priority

    def __repr__(self):
        return f"MiniTask(id={self.id}, title='{self.title}', priority='{self.priority}')"

# 1️⃣ Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("sprint.db")
cursor = conn.cursor()

# 2️⃣ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    priority TEXT NOT NULL
)
""")

conn.commit()

# 3️⃣ Insert data
cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", 
               ("Study SQL", "HIGH"))

cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", 
               ("Go Gym", "MEDIUM"))


conn.commit()

# 4️⃣ Read data
cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall()

tasks = []

for row in rows:
    task = MiniTask(row[0], row[1], row[2])
    tasks.append(task)

print("\nConverted to Objects:")
for task in tasks:
    print(task)

# 5️⃣ Update data
cursor.execute("UPDATE tasks SET priority = ? WHERE title = ?", 
               ("LOW", "Go Gym"))
conn.commit()

# 6️⃣ Read again
cursor.execute("SELECT * FROM tasks")
print("\nAfter Update:")
for row in cursor.fetchall():
    print(row)

# 7️⃣ Delete data
cursor.execute("DELETE FROM tasks WHERE title = ?", 
               ("Study SQL",))
conn.commit()

# 8️⃣ Final state
cursor.execute("SELECT * FROM tasks")
print("\nAfter Delete:")
for row in cursor.fetchall():
    print(row)

conn.close()