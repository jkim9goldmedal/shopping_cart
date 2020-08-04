def month_uriage_txt():
    from execute import sql_execute
    import pymysql
    from datetime import datetime,date,timedelta
    from dateutil.relativedelta import relativedelta

    today = datetime.today()
    today1 = datetime.strftime(today, '%Y%m')
    yestermonth = today - relativedelta(months=1)
    yestermonth1 = datetime.strftime(yestermonth, '%Y%m')
    filename = 'C:\\Users\\User\\Documents\\shopping_cart\\month_uriage\\Earnings_{}.txt'.format(yestermonth1)

    # try:

    f = open(filename,'w',encoding = 'utf-8')

    today2 = datetime.today()
    today3 = datetime.strftime(today, '%Y-%m')
    yestermonth2 = today2 - relativedelta(months=1)
    yestermonth3 = datetime.strftime(yestermonth2, '%Y-%m')

    print(yestermonth3,end = '\n',file=f)
    import month_data
    data = month_data.data_month()
    import month_column
    column = month_column.bat_column()
    import item_info_txt
    graph = item_info_txt.item_info(data,column)
    print(graph,file=f)
    print('=====================',file=f)
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    c = "select sum(case when 受注明細情報一覧.税率 = 10 then (税込金額 - 税抜金額) else 0 end) as '10%消費税合計',sum(case when 受注明細情報一覧.税率 = 8 then (税込金額 - 税抜金額) else 0 end) as '8%消費税合計'\
        from 受注明細情報一覧 inner join 受注 on 受注ID = 受注.id inner join 商品在庫一覧 on 受注明細情報一覧.商品番号 = 商品在庫一覧.商品番号\
        where DATE_FORMAT(受注.受注日, '%Y%m') = DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y%m')"
    cur.execute(c)
    tax = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    taxlist = []
    for x in tax:
        for y in x.values():
            taxlist.append(y)

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    b = "select sum(税込合計金額),sum(税抜合計金額),sum(税込送料込合計額),sum(税込配送料),sum(税抜配送料),削除フラグ,受注日,sum(税抜合計金額) + sum(税抜配送料)\
        from 受注\
        where DATE_FORMAT(受注日, '%Y%m') = DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y%m')"
    cur.execute(b)
    goukei = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for k in goukei:
        saigo = []
        for l in k.values():
            saigo.append(l)
        print('税込商品合計(税抜商品合計)',end = '',file=f)
        print(':'.rjust(6),end = '',file=f)
        print('{:,}'.format(saigo[0]).rjust(13),end = '',file=f)
        print('円(',end = '',file=f)
        print('{:,}'.format(saigo[1]).rjust(6),end = '',file=f)
        print('円)',file=f)
        print('税込配送料(税抜配送料)',end = '',file=f)
        print(':'.rjust(10),end = '',file=f)
        print('{:,}'.format(saigo[3]).rjust(13),end = '',file=f)
        print('円(',end = '',file=f)
        print('{:,}'.format(saigo[4]).rjust(6),end = '',file=f)
        print('円)',file=f)
        print('10%消費税合計',end = '',file=f)
        print(':'.rjust(18),end = '',file=f)
        print('{:,}'.format(taxlist[0]).rjust(13),end = '',file=f)
        print('円',file=f)
        print('8%消費税合計',end = '',file=f)
        print(':'.rjust(19),end = '',file=f)
        print('{:,}'.format(taxlist[1]).rjust(13),end = '',file=f)
        print('円',file=f)
        print('総額(税抜総額)',end = '',file=f)
        print(':'.rjust(17),end = '',file=f)
        print('{:,}'.format(saigo[2]).rjust(13),end = '',file=f)
        print('円(',end = '',file=f)
        print('{:,}'.format(saigo[7]).rjust(6),end = '',file=f)
        print('円)',file=f)
        print('====================',file=f)
    f.close()
    print('====================')
    print('ファイルは正常に' + filename + 'に保存されました。')

    # except:
    #     f.close()
    #     import os
    #     os.remove(filename)
    #     print('ERROR:ファイルの保存に失敗しました。')
    #
    # finally:
    #     if f:
    #         f.close()
