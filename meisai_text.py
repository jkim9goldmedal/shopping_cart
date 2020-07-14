def meisai_text(x):
    from execute import sql_execute
    import pymysql
    import os
    import datetime
    today1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    filename = 'C:\\Users\\user\\Documents\\shopping_cart\\meisai\\Bill_{}.txt'.format(today1)
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
        print('商品番号/商品名/商品詳細',end ='',file=f)
        print('税込価格/税抜価格/数量'.rjust(20,''),file=f)
        print('====================',file=f)

        for i in rows:
            meisai_list = []
            for j in i.values():
            print(meisai_list[1],end = '/',file=f)
            print(meisai_list[2],end = '/',file=f)
            print(meisai_list[3],end = ',',file=f)
            print('{:,}'.format(meisai_list[4]) + '円',end = '/',file=f)
            print('{:,}'.format(meisai_list[5]) + '円',end = '/',file=f)
            print('{:,}'.format(meisai_list[6]) + '個',end = '/\n',file=f)
        print('====================',file=f)

        import cart_keisan
        keisan = cart_keisan.keisan(x)
        print('税込商品合計(税抜商品合計)',end = '',file=f)
        print(':'rjust(5,''),end = '',file=f)
        print('{:,}'.format(keisan[0]).rjust(13,'')end = '',file=f)
        print('円(',end = '',file=f)
        print('{:,}'.format(keisan[1]).rjust(6,''),end = '',file=f)
        print('円)',file=f)
        print('税込配送料(税抜配送料)',end = '',file=f)
        print(':'.rjust(9,''),end = '',file=f)
        print('{;,}'.format(keisan[3]).rjust(13,''),end = '',file=f)
        print('円(',end = '',file=f)
        print('{:,}'.format(keisan[2]).rjust(6,''),end = '',file=f)
        print('円)',file=f)
        print('総額',end = '',file=f)
        print(':'.rjust(27,''),end = '',file=f)
        print('{:,}'.format(keisan[4]).rjust(13,''),end = '',file=f)
        print('円',file=f)

        f.close()
        print('ファイルは正常に' + filename + 'に保存されました。')

    except:
        f.close()
        os.remove(filename)
        print('ERROR:ファイルの保存に失敗しました。')

    finally:
        if f:
            f.close()
