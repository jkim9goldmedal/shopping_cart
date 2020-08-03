def cartnull(x):
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id),ログインID from カート group by ログインID  having ログインID = %s"
    cur.execute(p,x)
    cartcount = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return cartcount
