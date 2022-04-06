import mysql.connector
con=mysql.connector.connect(
    host="localhost",port="3306",
    user="root",password="abc123456",
    database="demo"
)
cursor=con.cursor()
sql="SELECT empno,ename,hiredate FROM t_emp;"
cursor.execute(sql)
for one in cursor:
    print(one[0],one[1],one[2])
con.close()