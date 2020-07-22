def rireki(x):
    from execute import sql_execute
    import pymysql
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select 受注.id,名前,受注日,顧客ID,税込合計金額,税抜合計金額,税込送料込合計額,税込配送料,税抜配送料\
        from 受注 inner join 顧客 on 顧客ID = 顧客.id\
        where 受注.削除フラグ = 0 and 顧客ID = %s"
    cur.execute(a,x)
    zyutyu = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    for i in zyutyu:#受注IDの取り出し
        zyutyu_list = []
        for j in i.values():#リストにIDを追加
            zyutyu_list.append(j)
        zyutyuid = zyutyu_list[0]

        print(zyutyu_list[2],end = '\n')
        import cart_column
        column = cart_column.column()
        import rireki_data
        data = rireki_data.data_rireki(zyutyuid)
        import item_info
        item_info.item_info(data,column)

        print('=====================')
        print('税込商品合計(税抜商品合計)',end = '')
        print(':'.rjust(5),end = '')
        print('{:,}'.format(zyutyu_list[4]).rjust(13),end = '')
        print('円(',end = '')
        print('{:,}'.format(zyutyu_list[5]).rjust(6),end = '')
        print('円)')
        print('税込配送料(税抜配送料)',end = '')
        print(':'.rjust(9),end = '')
        print('{:,}'.format(zyutyu_list[7]).rjust(13),end = '')
        print('円(',end = '')
        print('{:,}'.format(zyutyu_list[8]).rjust(6),end = '')
        print('円)')
        print('総額',end = '')
        print(':'.rjust(27),end = '')
        print('{:,}'.format(zyutyu_list[6]).rjust(13),end = '')
        print('円')
        print('====================')
