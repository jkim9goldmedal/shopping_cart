def zyutyu_null(x):
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id),受注日 from 受注 where 顧客ID = %s"
    cur.execute(p,x)
    zyutyucount = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return zyutyucount
