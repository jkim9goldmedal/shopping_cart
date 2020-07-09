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
            b = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(セール単価*(1+(税率/100)),0),セール単価,TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,在庫数,セールフラグ,均一フラグ\
                from 商品 inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                where 在庫数 > 0,削除フラグ = 0,商品カテゴリーID = {}\
                group by 商品番号".format(result)

            rows2 = sql_execute(b)
            print('商品番号/商品名/商品詳細/税込価格/税抜き価格')

            for k in rows2:
                if k[12] == '1':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[8]) + '円',end = '/')
                    print('{:,}'.format(k[9]) + '円',end = '/')
                    print()

                elif k[11] == '1':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[6]) + '円',end = '/')
                    print('{:,}'.format(k[7]) + '円',end = '/')
                    print()
                else:
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[4]) + '円',end = '/')
                    print('{:,}'.format(k[5]) + '円',end = '/')
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

            c = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(セール単価*(1+(税率/100)),0),セール単価,TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,在庫数,セールフラグ,均一フラグ\
                from 商品 inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                where 在庫数 > 0,削除フラグ = 0,商品名 like '%{}%'\
                group by 商品番号".format(result)

            rows3 = sql_execute(c)
            print('商品番号/商品名/商品詳細/税込価格/税抜き価格')
            for k in rows3:
                if k[12] == '1':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[8]) + '円',end = '/')
                    print('{:,}'.format(k[9]) + '円',end = '/')
                    print()
                elif k[11] == '1':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[6]) + '円',end = '/')
                    print('{:,}'.format(k[7]) + '円',end = '/')
                    print()
                else:
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[4]) + '円',end = '/')
                    print('{:,}'.format(k[5]) + '円',end = '/')
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

            d = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(セール単価*(1+(税率/100)),0),セール単価,TRUNCATE(均一単価*(1+(税率/100)),0),均一単価,在庫数,セールフラグ,均一フラグ\
                from 商品 inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
                where 在庫数 > 0,削除フラグ = 0,商品詳細 like '%{}%'\
                group by 商品番号".format(result)
            rows4 = sql_execute(d)
            print('商品番号/商品名/商品詳細/税込価格/税抜き価格')
            for k in rows4:
                if k[12] == '1':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[8]) + '円',end = '/')
                    print('{:,}'.format(k[9]) + '円',end = '/')
                    print()
                elif k[11] == '1':
                    print('【セール】')
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[6]) + '円',end = '/')
                    print('{:,}'.format(k[7]) + '円',end = '/')
                    print()
                else:
                    print(k[1],end = '/')
                    print(k[2],end = '/')
                    print(k[3],end = '/')
                    print('{:,}'.format(k[4]) + '円',end = '/')
                    print('{:,}'.format(k[5]) + '円',end = '/')
                    print()
            quitf = quitf + 1
            break
        else:
            print('正しい数字を入力してください。')
            quitf = quitf + 1
