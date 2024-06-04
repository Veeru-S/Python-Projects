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
cursor.execute('''INSERT INTO STUDENT VALUES (102,'Girish', 30)''') 
cursor.execute('''INSERT INTO STUDENT VALUES (103,'Veeresh', 18)''') 

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 

cursor.execute("DELETE FROM STUDENT WHERE age < 20")

conn.commit()
conn.close()