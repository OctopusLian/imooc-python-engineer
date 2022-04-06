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
    sql="INSERT INTO t_dept "\
        "(SELECT MAX(deptno)+10,%s,%s FROM t_dept UNION "\
        "SELECT MAX(deptno)+20,%s,%s FROM t_dept)"
    cursor=con.cursor()
    cursor.execute(sql,("A部门","北京","B部门","上海"))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)