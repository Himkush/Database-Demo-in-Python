import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("Himanshu.db")
c = conn.cursor()

def createTable():
         c.execute("CREATE TABLE IF NOT EXISTS student(rollno INTEGER, name TEXT, age INTEGER, marks REAL )")

def dynamic_data_entry():
         a = int(input("how many student:"))
         for i in range(a):
                  name = input("Enter the name of student:")
                  age = int(input("Enter the age of the student:"))
                  marks = float(input("Enter the marks of the student:"))
                  rollno = i+1
                  c.execute("INSERT INTO student(rollno, name, age, marks) VALUES(? ,? ,? ,?)",(rollno, name, age, marks))
         conn.commit()


def read_from_table():
         c.execute("SELECT *  FROM student")
         for row in c.fetchall():
                  print(row)

##createTable()
##dynamic_data_entry()
##
read_from_table()
c.close()
conn.close()
                  
         
