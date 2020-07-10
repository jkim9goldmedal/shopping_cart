def search_show():
    from execute import sql_execute
    quitf = 0
    while quitf < 1:
        a = "select id,カテゴリー from 商品カテゴリー where 削除フラグ = 0"

        rows = sql_execute(a)


        print('2:商品情報検索・一覧')
        choice = input('絞り込みたい項目を入力してください。(1:カテゴリーID　2:商品名 3:商品詳細) >')
        if choice == '1':
            print('カテゴリーID:カテゴリー名')
            print(")
            for i in rows:

                print(i[0], end = ':')
                print(i[1])
            sum = 0
            while sum < 1:
                category_choice = input('商品カテゴリーを入力してください。>')
                for j in rows:
                    if category_choice == j[0]:
                        kaku = input('{}で間違いないですか？（1:はい　2:いいえ）>').format(category_choice)
                        if kaku == '1':
                            result = j[0]
                            sum = sum + 1
                            break
                        if sum == 0:
                            print('もう一度入力してください。')
                    else:
                        print('間違った番号を入力しています。もう一度入力してください。')
    #SQLから該当するカテゴリー商品のリストを持ってくる。
    #０：id　１：商品番号　２：商品名　３：商品詳細　４：税込み販売単価　５：販売単価　６：商品割引税込み価格　７：商品割引税抜き価格　８：カテゴリー割引税込み価格　９：カテゴリー割引税抜き価格
    #１０：均一税込み　１１：均一価格　１２：在庫数　１３：割引フラグ　
            b = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(販売単価*(1-(商品割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(商品割引率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100)),0),TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,sum(変動在庫数) as 在庫数,割引フラグ\
                from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                where 在庫数 > 0,削除フラグ = 0,商品カテゴリーID = {}\
                group by 商品.id".format(result)


            rows2 = sql_execute(b)

            print('商品番号/商品名/商品詳細/税込価格/税抜き価格')

            for k in rows2:
                #均一価格表示
                if k[13] == '3':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[10]) + '円',end = '/')
                    print('{:,}'.format(k[11) + '円',end = '/')
                    print()

                elif k[13] == '2':
                    #カテゴリー割引率
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[8]) + '円',end = '/')
                    print('{:,}'.format(k[9]) + '円',end = '/')
                    print()
                elif k[13] == '0':
                    #定価
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[4]) + '円',end = '/')
                    print('{:,}'.format(k[5]) + '円',end = '/')
                    print()
                elif k[13] == '1':
                    #単品割引
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[6]) + '円',end = '/')
                    print('{:,}'.format(k[7]) + '円',end = '/')
                    print()
            quitf = quitf + 1
            break

        elif choice == '2':
            sum1 = 0
            while sum1 < 1:
                name_search = input('商品名を入力してください。(文字を含んでいれば検索可能) >')
                kaku = input('{}で間違いないですか？（1:はい　2:いいえ）>').format(name_search)
                if kaku =='1':
                    sum1 = sum1 + 1
                    result = name_search
                    break
                else:
                    print('もう一度入力してください。')

            c = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(販売単価*(1-(商品割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(商品割引率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100)),0),TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,sum(変動在庫数) as 在庫数,割引フラグ\
                from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                where 在庫数 > 0,削除フラグ = 0,商品名 like '%{}%'\
                group by 商品.id".format(result)

            rows3 = sql_execute(c)
            print('商品番号/商品名/商品詳細/税込価格/税抜き価格')
            for k in rows3:
                if k[13] == '3':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[10]) + '円',end = '/')
                    print('{:,}'.format(k[11) + '円',end = '/')
                    print()

                elif k[13] == '2':
                    #カテゴリー割引率
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[8]) + '円',end = '/')
                    print('{:,}'.format(k[9]) + '円',end = '/')
                    print()
                elif k[13] == '0':
                    #定価
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[4]) + '円',end = '/')
                    print('{:,}'.format(k[5]) + '円',end = '/')
                    print()
                elif k[13] == '1':
                    #単品割引
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[6]) + '円',end = '/')
                    print('{:,}'.format(k[7]) + '円',end = '/')
                    print()
            quitf = quitf + 1
            break
        elif choice == '3':
            sum2 = 0
            while sum2 < 1:
                namedet_search = input('商品名を入力してください。(文字を含んでいれば検索可能) >')
                kaku = input('{}で間違いないですか？（1:はい　2:いいえ）>').format(namedet_search)
                if kaku =='1':
                    sum2 = sum2 + 1
                    result = namedet_search
                    break
                else:
                    print('もう一度入力してください。')

            d = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(販売単価*(1-(商品割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(商品割引率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100)),0),TRUNCATE(販売単価*(1-(カテゴリー割引率/100)),0),TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,sum(変動在庫数) as 在庫数,割引フラグ\
                from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                where 在庫数 > 0,削除フラグ = 0,商品詳細 like '%{}%'\
                group by 商品.id".format(result)
            rows4 = sql_execute(d)
            print('商品番号/商品名/商品詳細/税込価格/税抜き価格')
            for k in rows4:
                if k[13] == '3':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[10]) + '円',end = '/')
                    print('{:,}'.format(k[11) + '円',end = '/')
                    print()

                elif k[13] == '2':
                    #カテゴリー割引率
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[8]) + '円',end = '/')
                    print('{:,}'.format(k[9]) + '円',end = '/')
                    print()
                elif k[13] == '0':
                    #定価
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[4]) + '円',end = '/')
                    print('{:,}'.format(k[5]) + '円',end = '/')
                    print()
                elif k[13] == '1':
                    #単品割引
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[6]) + '円',end = '/')
                    print('{:,}'.format(k[7]) + '円',end = '/')
                    print()
            quitf = quitf + 1
            break
        else:
            print('正しい数字を入力してください。')
