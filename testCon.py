import sqlite3

try:
    conn = sqlite3.connect('postlab.db')

except Exception as e:
    print("Error during connect:", str(e))

results = conn.execute("SELECT * FROM Customer")

for row in results:
    print (row)

conn.close()
