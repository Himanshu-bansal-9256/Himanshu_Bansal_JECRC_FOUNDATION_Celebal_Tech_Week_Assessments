import sqlite3

print("SQLite Version:", sqlite3.sqlite_version)

conn = sqlite3.connect("research_assistant.db")

print("Database Created Successfully!")

conn.close()