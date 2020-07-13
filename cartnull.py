def cartnull(x):
    from execute import sql_execute

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id) from カート where 顧客ID = %s group by 顧客ID"
    cartcount = cur.execute(p,x)
    cartcount = cur.fetchall()
    result = cartcount

    return result
