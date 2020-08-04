def zyutyu_null_day():
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id)\
        from 受注\
        where date_format(受注日 , '%Y/%m/%d') = date_sub(date(date_format( now() , '%Y/%m/%d')),interval 1 day)"
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
