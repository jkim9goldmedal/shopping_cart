def search_show():
    from execute import sql_execute
    import pymysql

    quitf = 0
    while quitf < 1:
        print('2:商品情報検索・一覧')
        choice = input('絞り込みたい項目を入力してください。(1:カテゴリーID　2:商品名 3:商品詳細) >')
        if choice == '1':
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            a = "select id,カテゴリー from 商品カテゴリー where 削除フラグ = 0"
            cur.execute(a)
            rows = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            print('カテゴリーID:カテゴリー名')
            print()

            for i in rows:
                category_list = []
                id,name = i.values()
                strid = str(id)
                category_list.append(strid)
                category_list.append(name)
                print(category_list[0] + ':' + category_list[1])
            category_list = []
            for i in rows:
                id,name = i.values()
                category_list.append(id)

            sum = 0
            while sum < 1:
                category_choice = int(input('カテゴリーIDを入力してください>'))
                if category_choice in category_list:
                    kaku = input(str(category_choice) + 'で間違いないですか？（1:はい　2:いいえ）>')
                    if kaku == '1':
                        result = str(category_choice)
                        sum = sum + 1
                        break
                    if sum == 0:
                        print('もう一度入力してください。')
                elif category_choice not in category_list:
                    print('入力が間違っています。もう一度入力してください。')


    #SQLから該当するカテゴリー商品のリストを持ってくる。
    #０：商品id　１：商品番号　２：商品名　３：商品詳細　４：税込み販売単価　５：販売単価　６：商品割引税込み価格　７：商品割引税抜き価格　８：カテゴリー割引税込み価格　９：カテゴリー割引税抜き価格
    #１０：均一税込み　１１：均一価格　１２：在庫数　１３：割引フラグ　14:削除フラグ　１５：商品カテゴリーID
            import search_null_id
            search_null_id.search_null_id(result)
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            b = "select 在庫.商品ID,商品番号,商品名,商品詳細,round(販売単価*(1+(税率/100))),販売単価,round(販売単価*(1-(商品割引率/100))*(1+(税率/100))),round(販売単価*(1-(商品割引率/100))),round(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100))),round(販売単価*(1-(カテゴリー割引率/100))),round(均一単価*(1+(税率/100))),均一単価,sum(在庫変動数),割引フラグ,商品.削除フラグ,商品カテゴリーID\
                from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                group by 在庫.商品ID\
                having 商品.削除フラグ = 0 and 商品カテゴリーID = %s and sum(在庫変動数) > 0"


            cur.execute(b,result)
            rows2 = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()

            print('商品番号/商品名/商品詳細/税込価格')
            for k in rows2:
                item_list = []
                for x in k.values():
                    item_list.append(x)

                #均一価格表示
                if item_list[13] == '3':

                    import kinitu_hyouzi
                    kinitu_hyouzi.kinitu_hyouzi(item_list)

                elif item_list[13] == '2':

                    import categorydis_hyouzi
                    categorydis_hyouzi.categorydis_hyouzi(item_list)
                elif item_list[13] == '0':

                    import teika_hyouzi
                    teika_hyouzi.teika_hyouzi(item_list)

                elif item_list[13] == '1':
                    #単品割引

                    import itemdis_hyouzi
                    itemdis_hyouzi.itemdis_hyouzi()
            quitf = quitf + 1
            break

        elif choice == '2':
            sum1 = 0
            while sum1 < 1:
                name_search = input('商品名を入力してください。(文字を含んでいれば検索可能) >')
                kaku = input(name_search + 'で間違いないですか？（1:はい　2:いいえ）>')
                if kaku =='1':
                    sum1 = sum1 + 1
                    result = '%' + name_search + '%'
                    break
                else:
                    print('もう一度入力してください。')
            import search_null
            search_null.search_null(result)
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            c = "select 在庫.商品ID,商品番号,商品名,商品詳細,round(販売単価*(1+(税率/100))),販売単価,round(販売単価*(1-(商品割引率/100))*(1+(税率/100))),round(販売単価*(1-(商品割引率/100))),round(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100))),round(販売単価*(1-(カテゴリー割引率/100))),round(均一単価*(1+(税率/100))),均一単価,sum(在庫変動数),割引フラグ,商品.削除フラグ,商品カテゴリーID\
                from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                group by 在庫.商品ID\
                having 商品.削除フラグ = 0 and 商品名 like %s and sum(在庫変動数) > 0"

            cur.execute(c,result)
            rows3 = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            print('商品番号/商品名/商品詳細/税込価格')
            for k in rows3:
                item_list = []
                for x in k.values():
                    item_list.append(x)

                if item_list[13] == '3':

                    import kinitu_hyouzi
                    kinitu_hyouzi.kinitu_hyouzi(item_list)

                elif item_list[13] == '2':
                    #カテゴリー割引率

                    import categorydis_hyouzi
                    categorydis_hyouzi.categorydis_hyouzi(item_list)
                elif item_list[13] == '0':
                    #定価

                    import teika_hyouzi
                    teika_hyouzi.teika_hyouzi(item_list)
                elif item_list[13] == '1':
                    #単品割引

                    import itemdis_hyouzi
                    itemdis_hyouzi.itemdis_hyouzi(item_list)
            quitf = quitf + 1
            break
        elif choice == '3':
            sum2 = 0
            while sum2 < 1:
                namedet_search = input('商品名を入力してください。(文字を含んでいれば検索可能) >')
                kaku = input(namedet_search + 'で間違いないですか？（1:はい　2:いいえ）>')
                if kaku =='1':
                    sum2 = sum2 + 1
                    result = '%' + namedet_search + '%'
                    break
                else:
                    print('もう一度入力してください。')
            import search_null_det
            search_null_det.search_null_det(result)
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            d = "select 在庫.商品ID,商品番号,商品名,商品詳細,round(販売単価*(1+(税率/100))),販売単価,round(販売単価*(1-(商品割引率/100))*(1+(税率/100))),round(販売単価*(1-(商品割引率/100)),0),round(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100))),round(販売単価*(1-(カテゴリー割引率/100))),round(均一単価*(1+(税率/100))),均一単価,sum(在庫変動数),割引フラグ,商品.削除フラグ,商品カテゴリーID\
                from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                group by 在庫.商品ID\
                having 商品.削除フラグ = 0 and 商品詳細 like %s and sum(在庫変動数) > 0"
            cur.execute(d,result)
            rows4 = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            print('商品番号/商品名/商品詳細/税込価格')
            print('========================================')
            for k in rows4:
                item_list = []
                for x in k.values():
                    item_list.append(x)

                if item_list[13] == '3':

                    import kinitu_hyouzi
                    kinitu_hyouzi.kinitu_hyouzi(item_list)

                elif item_list[13] == '2':
                    #カテゴリー割引率

                    import categorydis_hyouzi
                    categorydis_hyouzi.categorydis_hyouzi(item_list)
                elif item_list[13] == '0':
                    #定価

                    import teika_hyouzi
                    teika_hyouzi.teika_hyouzi(item_list)
                elif item_list[13] == '1':
                    #単品割引

                    import itemdis_hyouzi
                    itemdis_hyouzi.itemdis_hyouzi(item_list)
            quitf = quitf + 1
            break
        else:
            print('正しい数字を入力してください。')
