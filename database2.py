import sqlite3
import time
import datetime
import random
conn = sqlite3.connect("First.db")
c = conn.cursor()

def createTable():
         c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT,keyword TEXT, value REAL)')

def dataEntry():
         c.execute("INSERT INTO stuffToPlot VALUES(145, '2018-04-01', 'Python',5)")
         conn.commit()
         c.close()
         conn.close()

def dynamic_data_entry():
         unix = time.time()
         date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
         keyword = 'Himanshu'
         value = random.randrange(0,10)
         c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES( ?, ?, ?, ?)",
                   (unix, date, keyword,value))
         conn.commit()

def read_from_db():
         c.execute("SELECT  * FROM stuffToPlot WHERE value >=4 AND keyword = 'Himanshu'")
##         data = c.fetchall()
##         print(data)
         for row in c.fetchall():
                  print(row)
         
##createTable()
##
##for i in range(10):
##         dynamic_data_entry()
##         time.sleep(1)
read_from_db()
c.close()
conn.close()
