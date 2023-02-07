import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='vishal',passwd="1234",database='cheetsolution')

mycursor = mydb.cursor()

mycursor.execute("insert into student values ('Abhishek','MIT'),('Abhik','MITA'),('Abhi','MITB'),('shek','MITC')")

mycursor.execute("select * from student")
result = mycursor.fetchall()
#result = mycursor.fetchone()

for i in result:
    print(i)