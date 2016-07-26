import sqlite3
import pandas as pd
import pprint

db = sqlite3.connect("C:\Users\japau\Google Drive\Udacity\MongoDB\\"
                     "mongoDB_lesson_1_2429\py2.7go\SQL\chinook_db\chinook.db")

c = db.cursor()

QUERY = "SELECT DISTINCT Customer.CustomerId, Customer.LastName, Genre.Name " \
        "FROM InvoiceLine " \
        "JOIN Track ON InvoiceLine.TrackId = Track.TrackId " \
        "JOIN Genre on Track.GenreId = Genre.GenreId " \
        "JOIN Invoice ON InvoiceLine.InvoiceId = Invoice.InvoiceId " \
        "JOIN Customer ON Invoice.CustomerId = Customer.CustomerId " \
        "WHERE Genre.Name = 'Jazz'"

c.execute(QUERY)

rows = c.fetchall()

df = pd.DataFrame(rows)

db.close()

pprint.pprint(df)
