def zyutyu_null(x):
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id) from 受注 where ログインID = %s"
    cur.execute(p,x)
    zyutyucount = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    idlist = []
    for i in zyutyucount:
        for j in i.values():
            idlist.append(j)
    return idlist
