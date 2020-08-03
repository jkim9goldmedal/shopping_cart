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
                d = "select 商品番号,商品名,商品詳細,税込販売単価,税抜販売単価,税込商品割引価格,税抜商品割引価格,税込カテゴリー割引価格,税抜カテゴリー割引価格,税込均一価格,税抜均一単価,在庫数,割引フラグ,商品カテゴリー番号\
                    from 商品在庫一覧\
                    where 商品番号 = %s and 在庫数 > 0"
                cur.execute(d,a)
                rows = cur.fetchall()
                conn.commit()
                cur.close()
                conn.close()
                for row in rows:
                    cart_list = []
                    for k in row.values():
                        cart_list.append(k)
                    if a == cart_list[0]:
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
                                    if b <= cart_list[11]:
                                        zaiko = 0
                                        sum2 = 0
                                        conn = sql_execute()
                                        cur = conn.cursor(pymysql.cursors.DictCursor)
                                        cur.execute("USE shopping_cart")
                                        conn.commit()
                                        e = "select 商品番号,数量 from カート where ログインID = %s"
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
                                                    f = "UPDATE カート set 数量 = %s where 商品番号 = %s and ログインID = %s"
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
                                                    g = "delete from カート where 商品番号 = %s and ログインID = %s"
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
                                                if cart_list[12] == '0':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    h = "insert into カート(ログインID,商品番号,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(h,[x,cart_list[0],b,cart_list[3],cart_list[4]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif cart_list[12] == '1':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    i = "insert into カート(ログインID,商品番号,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(i,[x,cart_list[0],b,cart_list[5],cart_list[6]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif cart_list[12] == '2':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    j = "insert into カート(ログインID,商品番号,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(j,[x,cart_list[0],b,cart_list[7],cart_list[8]])
                                                    conn.commit()
                                                    cur.close()
                                                    conn.close()
                                                    print('==========')
                                                    print('カートに追加しました。')
                                                    add = add + 1
                                                elif cart_list[12] == '3':
                                                    conn = sql_execute()
                                                    cur = conn.cursor(pymysql.cursors.DictCursor)
                                                    cur.execute("USE shopping_cart")
                                                    conn.commit()
                                                    k = "insert into カート(ログインID,商品番号,数量,税込価格,税抜価格) values(%s,%s,%s,%s,%s)"
                                                    cur.execute(k,[x,cart_list[0],b,cart_list[9],cart_list[10]])
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
