import sqlite3

conn = sqlite3.connect("First.db")

c = conn.cursor()

def createTable():
         c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT,keyword TEXT, value REAL)')

def dataEntry():
         c.execute("INSERT INTO stuffToPlot VALUES(145, '2018-04-01', 'Python',5)")
         conn.commit()
         c.close()
         conn.close()

createTable()
dataEntry()
