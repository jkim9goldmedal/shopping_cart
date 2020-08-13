def meisai_text(x):
    from execute import sql_execute
    import pymysql
    import datetime
    today1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")




    today2 = datetime.datetime.now().strftime("%Y/%m/%d")
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    name = "select 名前,ログインID,郵便番号,住所 from 顧客一覧 where ログインID = %s"
    cur.execute(name,x)
    rows5 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for y in rows5:
        name_list = []
        for z in y.values():
            name_list.append(z)
    filename = 'C:\\Users\\User\\Documents\\shopping_cart\\meisai\\Bill_{}_{}.txt'.format(name_list[0],today1)

    f = open(filename,'w',encoding = 'utf-8')
    print(name_list[0] + '様',end = '\n',file=f)
    print('〒' + name_list[2],end = '\n',file=f)
    print('住所:' + name_list[3],end = '\n',file=f)
    print(today2,end = '\n',file=f)
    print('====================',file=f)
    import cart_data
    data = cart_data.data_cart(x)
    import item_info_txt
    import cart_column
    column = cart_column.column()

    graph = item_info_txt.item_info(data,column)
    print(graph,file=f)

    print('====================',file=f)

    import cart_keisan
    keisan = cart_keisan.keisan(x)
    print('税込商品合計(税抜商品合計)',end = '',file=f)
    print(':'.rjust(5),end = '',file=f)
    print('{:,}'.format(keisan[0]).rjust(13),end = '',file=f)
    print('円(',end = '',file=f)
    print('{:,}'.format(keisan[1]).rjust(6),end = '',file=f)
    print('円)',file=f)
    print('税込配送料(税抜配送料)',end = '',file=f)
    print(':'.rjust(9),end = '',file=f)
    print('{:,}'.format(keisan[3]).rjust(13),end = '',file=f)
    print('円(',end = '',file=f)
    print('{:,}'.format(keisan[2]).rjust(6),end = '',file=f)
    print('円)',file=f)
    print('総額',end = '',file=f)
    print(':'.rjust(25),end = '',file=f)
    print('{:,}'.format(keisan[4]).rjust(12),end = '',file=f)
    print('円',file=f)
    print('====================',file=f)
    print('振込先情報\nvv銀行\n赤坂支店\n口座番号:1234567\n名義：カトウアツシ',file=f)
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
    #     f.close()
