import sqlite3

# Path to your database file
db_path = "data/metrics.db"

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List all tables
print("\n📋 Tables in database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for t in tables:
    print(" -", t[0])

# Show first few rows from metrics table
print("\n📊 Sample data from metrics:")
cursor.execute("SELECT * FROM metrics LIMIT 5;")
for row in cursor.fetchall():
    print(row)

# Show alerts too
print("\n⚠️ Sample data from alerts:")
cursor.execute("SELECT * FROM alerts LIMIT 5;")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
