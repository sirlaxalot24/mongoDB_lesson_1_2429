import sqlite3
import pandas as pd
import pprint

db = sqlite3.connect("C:\Users\japau\Google Drive\Udacity\MongoDB\\"
                     "mongoDB_lesson_1_2429\py2.7go\SQL\chinook_db\chinook.db")


c = db.cursor()

QUERY = "SELECT Genre.Name, count(Genre.Name) as genCnt " \
        "FROM Track " \
        "JOIN Genre ON Track.GenreId = Genre.GenreId " \
        "WHERE Track.Milliseconds < " \
        "(SELECT avg(Track.Milliseconds) FROM Track) " \
        "GROUP BY Genre.Name " \
        "ORDER BY genCnt DESC"


c.execute(QUERY)

rows = c.fetchall()

df = pd.DataFrame(rows)

db.close()

pprint.pprint(df)
