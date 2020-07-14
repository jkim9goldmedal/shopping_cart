def cart_meisai(x):
    from execute import sql_execute
    import pymysql
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select カート.商品ID,商品番号,商品.商品名,商品詳細,税込価格,税抜価格,数量,税率,顧客ID\
        from カートinner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
        group by 商品.id\
        having 顧客ID = %s"
    cur.execute(a,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    print('商品番号/商品名/商品詳細',end = ")
    print('税込価格/税抜価格/数量'.rjust(20,''))
    print('====================')
    for i in rows:
        meisai_list = []
        for j in i.values():
            meisai_list.append(j)
        print(meisai_list[1],end = '/')
        print(meisai_list[2],end = '/')
        print(meisai_list[3],end = ',')
        print('{:,}'.format(meisai_list[4]) + '円',end = '/')
        print('{:,}'.format(meisai_list[5]) + '円',end = '/')
        print('{:,}'.format(meisai_list[6]) + '個',end = '/')
        print()

    print('=====================')
    import cart_keisan
    keisan = cart_keisan.keisan(x)
    print('税込商品合計(税抜商品合計)',end = '')
    print(':'rjust(5,''),end = '')
    print('{:,}'.format(keisan[0]).rjust(13,'')end = '')
    print('円(',end = '')
    print('{:,}'.format(keisan[1]).rjust(6,''),end = '')
    print('円)')
    print('税込配送料(税抜配送料)',end = '')
    print(':'.rjust(9,''),end = '')
    print('{;,}'.format(keisan[3]).rjust(13,''),end = '')
    print('円(',end = '')
    print('{:,}'.format(keisan[2]).rjust(6,''),end = '')
    print('円)')
    print('総額',end = '')
    print(':'.rjust(27,''),end = '')
    print('{:,}'.format(keisan[4]).rjust(13,''),end = '')
    print('円')
