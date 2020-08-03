def cart_syori(x):
    from execute import sql_execute
    import pymysql
    import cart_keisan
    keisan = cart_keisan.keisan(x)
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    uriage = "insert into 受注(ログインID,受注日,税込合計金額,税抜合計金額,税込送料込合計額,注文合計数,税込配送料,税抜配送料)\
        values(%s,cast(now() as date),%s,%s,%s,%s,%s,%s)"

    cur.execute(uriage,[x,keisan[0],keisan[1],keisan[4],keisan[5],keisan[3],keisan[2]])
    conn.commit()
    cur.close()
    conn.close()

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    zyutyu_id = "select MAX(id) from 受注 where ログインID = %s"
    cur.execute(zyutyu_id,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for i in rows:
        id_list = []
        for j in i.values():
            id_list.append(j)
        zyutyuid = id_list[0]
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    cartmeisai = "select 商品番号,税込価格*数量,税抜価格*数量,税抜価格,数量,税込価格\
                from カート\
                where ログインID = %s"
    cur.execute(cartmeisai,x)
    rows1 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for k in rows1:
        cartmeisai_list = []
        for l in k.values():
            cartmeisai_list.append(l)
        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        meisai = "insert into 受注明細(受注ID,数量,税込金額,税抜金額,商品番号,販売単価,税込販売単価) values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(meisai,[zyutyuid,cartmeisai_list[4],cartmeisai_list[1],cartmeisai_list[2],cartmeisai_list[0],cartmeisai_list[3],cartmeisai_list[5]])
        conn.commit()
        cur.close()
        conn.close()
    #在庫引き当て
        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        cartmeisai_list[4]
        cartmeisai_list[4] = -cartmeisai_list[4]
        zaiko = "insert into 在庫(日付,在庫変動数,商品番号,在庫確認フラグ) values(cast(now() as date),%s,%s,2)"
        cur.execute(zaiko,[cartmeisai_list[4],cartmeisai_list[0]])
        conn.commit()
        cur.close()
        conn.close()
    import cartdel
    cartdel.cartdel(x)
