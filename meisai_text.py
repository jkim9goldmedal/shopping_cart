def meisai_text(x):
    from execute import sql_execute
    import pymysql
    import datetime
    today1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    filename = 'C:\\Users\\User\\Documents\\shopping_cart\\meisai\\Bill_{}.txt'.format(today1)
    try:
        f = open(filename,'w')
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
        f.write('商品番号/商品名/商品詳細',end ='')
        f.write('税込価格/税抜価格/数量'.rjust(20))
        f.write('====================')

        for i in rows:
            meisai_list = []
            for j in i.values():
                meisai_list.append(j)
            f.write(meisai_list[1],end = '/')
            f.write(meisai_list[2],end = '/')
            f.write(meisai_list[3],end = ',')
            f.write('{:,}'.format(meisai_list[4]) + '円',end = '/')
            f.write('{:,}'.format(meisai_list[5]) + '円',end = '/')
            f.write('{:,}'.format(meisai_list[6]) + '個',end = '\n')
        f.write('====================')

        import cart_keisan
        keisan = cart_keisan.keisan(x)
        f.write('税込商品合計(税抜商品合計)',end = '')
        f.write(':'.rjust(5),end = '')
        f.write('{:,}'.format(keisan[0]).rjust(13),end = '')
        f.write('円(',end = '')
        f.write('{:,}'.format(keisan[1]).rjust(6),end = '')
        f.write('円)')
        f.write('税込配送料(税抜配送料)',end = '')
        f.write(':'.rjust(9),end = '')
        f.write('{:,}'.format(keisan[3]).rjust(13),end = '')
        f.write('円(',end = '')
        f.write('{:,}'.format(keisan[2]).rjust(6),end = '')
        f.write('円)')
        f.write('総額',end = '')
        f.write(':'.rjust(27),end = '')
        f.write('{:,}'.format(keisan[4]).rjust(13),end = '')
        f.write('円')
        f.write('====================')
        f.write('振込先情報\nvv銀行\n赤坂支店\n口座番号:1234567\n名義：カトウアツシ')
        f.write('====================')
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
