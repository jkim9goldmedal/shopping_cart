def zaikocheck(x):
    from execute import sql_execute
    import pymysql


    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select 商品番号,数量 from カート where ログインID = %s"
    cur.execute(a,x)
    row1 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()


    for ro in row1:
        cart_list = []
        a,b = ro.values()
        cart_list.append(a)
        cart_list.append(b)
        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        d = "select 商品番号,商品名,在庫数\
            from 商品在庫一覧 where 商品番号 = %s"
        cur.execute(d,cart_list[0])
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        for row in rows:
            item_list = []
            c,d,e = row.values()
            item_list.append(c)
            item_list.append(d)
            item_list.append(e)


            check = 0
            if cart_list[1] > int(item_list[2]):
                conn = sql_execute()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("USE shopping_cart")
                conn.commit()
                cartdel = "delete from カート where ログインID = %s and 商品番号 = %s"
                cur.execute(cartdel,[x,cart_list[0]])
                conn.commit()
                cur.close()
                conn.close()

                print(item_list[1] + 'の在庫が足りません。カートから削除します。')
                check += 1


            else:
                print('在庫チェックが完了しました。')
            return check
