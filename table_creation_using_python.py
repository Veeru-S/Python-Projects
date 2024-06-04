import sqlite3

conn=sqlite3.connect("veeru.db")
cursor=conn.cursor()

cursor.execute("drop table if exists student")

table='''create table STUDENT (
rollno int,name char(25), age int
);'''

cursor.execute(table)
print("Table is Ready")

cursor.execute('''INSERT INTO STUDENT VALUES (101,'Veeru', 21)''') 
cursor.execute('''INSERT INTO STUDENT VALUES (102,'Girish', 28)''') 
cursor.execute('''INSERT INTO STUDENT VALUES (103,'Veeresh', 18)''') 
cursor.execute('''INSERT INTO STUDENT VALUES (104,'Modi', 82)''') 
cursor.execute('''INSERT INTO STUDENT VALUES (105,'Veerendra', 28)''') 

print("Data Inserted in the table: ") 

cursor.execute('''UPDATE STUDENT SET AGE = 0 WHERE name='Modi';''') 

cursor.execute('''SELECT * FROM STUDENT WHERE age=28''') 

cursor.execute('''DELETE FROM STUDENT WHERE age < 20''')

data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 

conn.commit()
conn.close()
