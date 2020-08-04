def day_uriage_txt():
    from execute import sql_execute
    import pymysql
    from datetime import datetime,date,timedelta
    today = datetime.today()
    today1 = datetime.strftime(today, '%Y%m%d')
    yesterday = today - timedelta(days=1)
    yesterday1 = datetime.strftime(yesterday, '%Y%m%d')

    filename = 'C:\\Users\\User\\Documents\\shopping_cart\\day_uriage\\Earnings_{}.txt'.format(yesterday1)
    try:
        f = open(filename,'w',encoding = 'utf_8_sig')
        today2 = datetime.today()
        today3 = datetime.strftime(today, '%Y-%m-%d')
        yesterday2 = today - timedelta(days=1)
        yesterday3 = datetime.strftime(yesterday, '%Y-%m-%d')

        print('====================',file=f)
        print(yesterday3,end = '\n',file=f)
        import data
        data = data.data()
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
        b = "select sum(税込合計金額),sum(税抜合計金額),sum(税込送料込合計額),sum(税込配送料),sum(税抜配送料),削除フラグ,受注日,sum(税抜合計金額) + sum(税抜配送料)\
            from 受注\
            where date_format(受注日 , '%Y/%m/%d') = date_sub(date(date_format( now() , '%Y/%m/%d')),interval 1 day)"
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
            print(':'.rjust(5),end = '',file=f)
            print('{:,}'.format(saigo[0]).rjust(13),end = '',file=f)
            print('円(',end = '',file=f)
            print('{:,}'.format(saigo[1]).rjust(6),end = '',file=f)
            print('円)',file=f)
            print('税込配送料(税抜配送料)',end = '',file=f)
            print(':'.rjust(9),end = '',file=f)
            print('{:,}'.format(saigo[3]).rjust(13),end = '',file=f)
            print('円(',end = '',file=f)
            print('{:,}'.format(saigo[4]).rjust(6),end = '',file=f)
            print('円)',file=f)
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
    except:
        f.close()
        import os
        os.remove(filename)
        print('ERROR:ファイルの保存に失敗しました。')
    finally:
        if f:
            f.close()
