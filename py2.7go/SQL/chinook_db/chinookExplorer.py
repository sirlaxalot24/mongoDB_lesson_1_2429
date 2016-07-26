import sqlite3


db = sqlite3.connect("C:\Users\japau\Google Drive\Udacity\MongoDB\\"
                     "mongoDB_lesson_1_2429\py2.7go\SQL\chinook_db\chinook.db")

c = db.cursor()

tableQuery = "SELECT name FROM sqlite_master WHERE type='table';"

c.execute(tableQuery)

rows = c.fetchall()

for i in rows:
    QUERY = "pragma table_info('%s')" % i
    c.execute(QUERY)
    table = c.fetchall()
    print i[0]
    for x in table:
        print x[1:]
    print ""

db.close()
