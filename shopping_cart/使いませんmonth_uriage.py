def month_uriage():
    import pymysql
    from execute import sql_execute
    import datetime
    today = datetime.datetime.now().strftime("%Y/%m")
    print('====================')
    print(today,end = '\n')

    import month_data
    data = month_data.data_month()
    import column
    column = column.column()
    import item_info
    item_info.item_info(data,column)
    print('=====================')
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    b = "select sum(税込合計金額),sum(税抜合計金額),sum(税込送料込合計額),sum(税込配送料),sum(税抜配送料),削除フラグ,受注日,sum(税抜合計金額) + sum(税抜配送料)\
        from 受注\
        where DATE_FORMAT(受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m') and 削除フラグ = 0"
    cur.execute(b)
    goukei = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for k in goukei:
        saigo = []
        for l in k.values():
            saigo.append(l)
        print('税込商品合計(税抜商品合計)',end = '')
        print(':'.rjust(5),end = '')
        print('{:,}'.format(saigo[0]).rjust(13),end = '')
        print('円(',end = '')
        print('{:,}'.format(saigo[1]).rjust(6),end = '')
        print('円)')
        print('税込配送料(税抜配送料)',end = '')
        print(':'.rjust(9),end = '')
        print('{:,}'.format(saigo[3]).rjust(13),end = '')
        print('円(',end = '')
        print('{:,}'.format(saigo[4]).rjust(6),end = '')
        print('円)')
        print('総額(税抜総額)',end = '')
        print(':'.rjust(17),end = '')
        print('{:,}'.format(saigo[2]).rjust(13),end = '')
        print('円(',end = '')
        print('{:,}'.format(saigo[7]).rjust(6),end = '')
        print('円)')
        print('====================')
