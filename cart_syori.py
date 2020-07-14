def cart_syori(x):
    from execute import sql_execute
    import pymysql
    import cart_keisan
    keisan = cart_keisan.keisan(x)
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    uriage = "insert into 受注(顧客ID,受注日,税込合計金額,税抜合計金額,税込送料込合計額)"
    cur.execute(uriage,x)
    conn.commit()
    cur.close()
    conn.close()
