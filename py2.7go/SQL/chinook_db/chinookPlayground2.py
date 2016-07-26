import sqlite3
import pandas as pd
import pprint

db = sqlite3.connect("C:\Users\japau\Google Drive\Udacity\MongoDB\\"
                     "mongoDB_lesson_1_2429\py2.7go\SQL\chinook_db\chinook.db")

c = db.cursor()

QUERY = "SELECT Track.Name, MediaType.Name, Genre.Name " \
        "FROM Track " \
        "JOIN Genre ON Track.GenreId = Genre.GenreId " \
        "JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId " \
        "WHERE Genre.Name = 'Pop' and MediaType.Name = 'MPEG audio file'"

c.execute(QUERY)

rows = c.fetchall()

df = pd.DataFrame(rows)

db.close()

pprint.pprint(df)
