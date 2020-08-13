def data_cart(x):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select カート.商品番号,商品在庫一覧.商品名,商品詳細,税込価格,税抜価格,数量,税率,ログインID,税込価格*数量\
        from カート inner join 商品在庫一覧 on カート.商品番号 = 商品在庫一覧.商品番号\
        where ログインID = %s\
        group by カート.商品番号"
    cur.execute(a,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    data = []
    for i in rows:
        column_list = []
        itemcode,name,namedet,taxprice,price,num,zeiritu,cusid,syoukei = i.values()
        num = str(num) + '個'
        taxprice = str(taxprice) + '円'
        price = '(' + str(price) + '円)'
        syoukei = str(syoukei) + '円'


        column_list = [itemcode,name,namedet,taxprice,price,num,syoukei]

        data.append(column_list)

    return data
