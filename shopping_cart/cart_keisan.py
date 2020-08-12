def keisan(x):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select sum(税込価格*数量),sum(税抜価格*数量),sum(数量)\
        from カート\
        where ログインID = %s"
    cur.execute(a,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    haisou = 0
    haisoutax = 0
    for row in rows:
        cart_list = []
        for k in row.values():
            cart_list.append(k)
        if cart_list[1] < 10000:
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            b = "select round(配送料*(1+(税率/100))),配送料,顧客一覧.ログインID\
                from 顧客一覧 inner join 配送料一覧 on 顧客一覧.配送料管理番号 = 配送料一覧.配送料管理番号 inner join 税率一覧 on 配送料一覧.税率管理番号 = 税率一覧.税率管理番号\
                where 顧客一覧.ログインID = %s"
            cur.execute(b,x)
            rows1 = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            for j in rows1:
                haisou_list =[]
                for k in j.values():
                    haisou_list.append(k)
                haisou = round(haisou_list[1])
                haisoutax = round(haisou_list[0])

        elif cart_list[1] >= 10000:
            haisou = 0

            haisoutax = 0

        # cart_list[0]
        # cart_list[0] = int(round(cart_list[0]))
        # cart_list[1]
        # cart_list[1] = int(round(cart_list[1]))

        sougaku = cart_list[0] + haisoutax
        goukeitax = cart_list[0]
        goukei = cart_list[1]
        ordersum = cart_list[2]
        return goukeitax,goukei,haisou,haisoutax,sougaku,ordersum
