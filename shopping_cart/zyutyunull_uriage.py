def zyutyu_null_day():
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id)\
        from 受注\
        where 受注日 = cast(now() as date)"
    cur.execute(p)
    zyutyucount = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return zyutyucount
