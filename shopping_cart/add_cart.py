def add_cart(x):
    from execute import sql_execute
    import pymysql
    add = 0
    while add < 1:
        sum = 0
        a = input('購入する商品番号を入力してください。購入しない場合はNGを入力>')
        bangoukaku = input(a + 'で間違いないですか？（1:はい 2:いいえ）>')
        if bangoukaku == '1':
            if a == 'NG':
                add += 1
                break
            else:
                conn = sql_execute()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("USE shopping_cart")
                conn.commit()
                d = "select 在庫.商品ID,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(販売単価*(1-(商品割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(商品割引率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100)),0),TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,sum(在庫変動数),割引フラグ,商品.削除フラグ,商品カテゴリーID\
                    from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                    group by 在庫.商品ID\
                    having 商品.削除フラグ = 0 and 商品番号 = %s and sum(在庫変動数) > 0"
                cur.execute(d,a)
                rows = cur.fetchall()
                conn.commit()
                cur.close()
                conn.close()
                for row in rows:
                    cart_list = []
                    for k in row.values():
                        cart_list.append(k)
                    if a == cart_list[1]:
                        sum = sum + 1
                        try:
                            print('==========')
                            b = int(input('購入する数量を入力してください。>'))
                            kazukaku = input(str(b) + '個で間違いないですか？（1:はい 2:いいえ）>')
                            if kazukaku =='1':
                                if b > 5:
                                    print('==========')
                                    print('カートに追加できるのは5個までです。入力しなおしてください。')
                                elif b == 0:
                                    print('==========')
                                    print('0でない数を入力してください。')
                                else:
                                    if b <= cart_list[12]:
                                        zaiko = 0
                                        sum2 = 0
                                        conn = sql_execute()
                                        cur = conn.cursor(pymysql.cursors.DictCursor)
                                        cur.execute("USE shopping_cart")
                                        conn.commit()
                                        e = "select 商品ID,数量 from カート where 顧客ID = %s"
                                        cur.execute(e,x)
                                        rows2 = cur.fetchall()
                                        conn.commit()
                                        cur.close()
                                        conn.close()
                                        for row2 in rows2:
                                            list = []
                                            for k in row2.values():
                                                list.append(k)
                                            if cart_list[0] == list[0]:
                                                sum2 = sum2 + 1
                                                zaiko = b + list[1]
                                                if zaiko <= 5 and zaiko > 0:
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    f = "UPDATE カート set 数量 = %s where 商品ID = %s and 顧客ID = %s"
                                                    cur.execute(f,[zaiko,cart_list[0],x])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif zaiko > 5:
                                                    print('==========')
                                                    print('カートに入れられる商品は5個までです。入力しなおしてください。')
                                                elif zaiko <= 0:
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    g = "delete from カート where 商品ID = %s and 顧客ID = %s"
                                                    cur.execute(g,[cart_list[0],x])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートの商品数が0になったのでカートから削除します。')
                                                    add = add + 1
                                        if sum2 == 0:
                                            if b < 0:
                                                print('==========')
                                                print('カートにない商品は減らせません。入力しなおしてください。')
                                            else:
                                                if cart_list[13] == '0':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    h = "insert into カート(顧客ID,商品ID,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(h,[x,cart_list[0],b,cart_list[4],cart_list[5]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif cart_list[13] == '1':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    i = "insert into カート(顧客ID,商品ID,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(i,[x,cart_list[0],b,cart_list[6],cart_list[7]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif cart_list[13] == '2':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    j = "insert into カート(顧客ID,商品ID,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(j,[x,cart_list[0],b,cart_list[8],cart_list[9]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif cart_list[13] == '3':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    k = "insert into カート(顧客ID,商品ID,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(k,[x,cart_list[0],b,cart_list[10],cart_list[11]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1

                                        break
                                    else:
                                        print('==========')
                                        print('在庫がありません。入力しなおしてください。')
                                        sum += 1
                            elif kazukaku == '2':
                                print('==========')
                                print('入力しなおしてください。')
                        except ValueError as ve:
                            print('==========')
                            print('入力内容が間違っています。もう一度入力してください。')


        if sum == 0 or bangoukaku =='2':
            print('==========')
            print('入力内容が間違っているか、商品番号が間違っています。\nもう一度商品番号から入力してください。')
