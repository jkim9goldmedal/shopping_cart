def zyutyu_null_month():
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id) from 受注 where DATE_FORMAT(受注日, '%Y%m') = DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y%m')"
    cur.execute(p)
    zyutyucount = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    idlist = []
    for i in zyutyucount:
        for j in i.values():
            idlist.append(j)
    return idlist
