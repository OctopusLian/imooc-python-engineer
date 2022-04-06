import mysql.connector.pooling

config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"abc123456",
    "database":"demo"
}
try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con=pool.get_connection()
    con.start_transaction()
    cursor=con.cursor()
    sql="INSERT INTO t_dept(deptno,dname,loc) VALUES(%s,%s,%s)"
    data=[
        [100,"A部门","北京"],[110,"B部门","上海"]
    ]
    cursor.executemany(sql,data)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)