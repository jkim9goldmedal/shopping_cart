def cartnull_add(x):
    from execute import sql_execute
    import pymysql

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    p = "select count(id),顧客ID\
        from カート\
        group by 顧客ID\
        having 顧客ID = %s"
    cur.execute(p,x)
    cartcount = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if cartcount == ():
        print('カート内に商品はありません。')
    else:
        print('カート内に商品があります。')
