def data_cart(x):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select カート.商品ID,商品番号,商品.商品名,商品詳細,税込価格,税抜価格,数量,税率,顧客ID\
        from カート inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
        group by 商品.id\
        having 顧客ID = %s"
    cur.execute(a,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    data = []
    for i in rows:
        column_list = []
        id,itemcode,name,namedet,taxprice,price,num,zeiritu,cusid = i.values()
        num = str(num) + '個'
        taxprice = str(taxprice) + '円'
        price = '(' + str(price) + '円)'

        column_list = [itemcode,name,namedet,taxprice,price,num]

        data.append(column_list)

    return data
