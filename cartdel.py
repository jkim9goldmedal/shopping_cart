def cartdel(x):
    from execute import sql_execute
    import pymysql
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    cartdel = "delete from カート where 顧客ID = %s"
    cur.execute(cartdel,x)
    conn.commit()
    cur.close()
    conn.close()
