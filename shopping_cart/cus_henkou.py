def henkou(x):
    from execute import sql_execute
    import pymysql
    stop = 0
    while stop < 1:

        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        a = "select id,名前,カナ,郵便番号,住所,電話番号,配送料管理番号,メールアドレス,ログインID,ログインパスワード\
            from 【ログイン用】顧客一覧\
            where ログインID = %s"

        cur.execute(a,x)
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        print('変更を行います。')
        cus_list = []
        for i in rows:

            for j in i.values():
                cus_list.append(j)
        # conn = sql_execute()
        # cur = conn.cursor(pymysql.cursors.DictCursor)
        # cur.execute("USE shopping_cart")
        # conn.commit()
        # cus = "insert into 顧客(名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインパスワード,削除フラグ,備考)\
        #     values(%s,%s,%s,%s,%s,%s,%s,%s,%s,1,cast(now()as date))"
        # cur.execute(cus,[cus_list[1],cus_list[2],cus_list[3],cus_list[4],cus_list[5],cus_list[6],cus_list[7],cus_list[8],cus_list[9]])
        # conn.commit()
        # cur.close()
        # conn.close()

        # henkou = input('変更したい項目を入力してください。>')
        # henkounaiyou = input('変更後の内容を入力してください。>')

        while True:
            henkou = input('変更したい項目を入力してください。\n1:名前\n2:カナ\n3:郵便番号\n4:住所\n5:電話番号\n6:配送料管理番号\n7:メールアドレス\n8:ログインパスワード\n>')
            if henkou == '1':
                name = input('名前（40文字以内）>')
                checkname = len(name)
                if "'" in name or '"' in name or "’" in name or '”' in name:
                    print('入力内容が間違っています。もう一度入力してください。')
                elif 1 <= checkname <= 40:

                    namekaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if namekaku == '1':
                        cus_list[1] = name

                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数が間違っています。もう一度入力してください。')
            elif henkou == '2':
                kana = input('カナ（40文字以内）>')
                checkkana = len(kana)
                if "'" in kana or '"' in kana or "’" in kana or '”' in kana:
                    print('入力内容が間違っています。もう一度入力してください。')
                elif 1 <= checkkana <= 40:

                    kanakaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if kanakaku == '1':
                        cus_list[2] = kana
                        break

                    else:
                        print('入力しなおしてください。')
            elif henkou == '3':
                try:
                    zipcode = int(input('郵便番号（7桁）>'))
                except ValueError as ve:
                    print('数字以外を入力しています。もう一度入力してください。')
                else:
                    zipcodestr = str(zipcode)
                    checkzipcode = len(zipcodestr)
                    if checkzipcode == 7:

                        zipkaku = input('間違いないですか？（1:はい　2:いいえ）')
                        if zipkaku == '1':
                            cus_list[3] = str(zipcode)
                            break

                        else:
                            print('入力しなおしてください。')
                    else:
                        print('入力文字数が間違っています。もう一度入力してください。')
            elif henkou == '4':
                address = input('住所（100文字以内）>')
                checkaddress = len(address)
                if "'" in address or '"' in address or "’" in address or '”' in address:
                    print('入力内容が間違っています。もう一度入力してください。')
                elif 1 <= checkaddress <= 100:

                    addkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if addkaku == '1':
                        cus_list[4] = address
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数が間違っています。もう一度入力してください。')
            elif henkou == '5':
                try:
                    tel = int(input('電話番号（10-11文字以内）最初の「0」は除いて入力してください。\n例:09012345678→9012345678\n>'))
                    tel1 = '0' + str(tel)
                except ValueError as ve:
                    print('数字以外を入力しています。もう一度入力してください。')
                else:
                    telstr = str(tel)
                    checktel = len(telstr)
                    if 9 <= checktel <= 10:

                        telkaku = input('間違いないですか？（1:はい　2:いいえ）')
                        if telkaku == '1':
                            cus_list[5] = tel1
                            break
                        else:
                            print('入力しなおしてください。')
                    else:
                        print('入力文字数が間違っています。もう一度入力してください。')

            elif henkou == '6':
                try:
                    conn = sql_execute()
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("USE shopping_cart")
                    conn.commit()
                    h = "select 配送料管理番号,地域 from 配送料一覧"
                    cur.execute(h)
                    hlist = cur.fetchall()
                    conn.commit()
                    cur.close()
                    conn.close()
                    for hh in hlist:
                        hhlist= []
                        hnum,area = hh.values()
                        hhlist.append(hnum)
                        hhlist.append(area)
                        print(str(hhlist[0]) + ':' + hhlist[1])
                    haisouryou = int(input('住所に該当する配送料の番号を入力してください。>'))
                except ValueError as ve:
                    print('数字以外を入力しています。もう一度入力してください。')
                else:
                    hhlist= []
                    for hh in hlist:
                        hnum,area = hh.values()
                        hhlist.append(hnum)
                        hhlist.append(area)
                    if haisouryou in hhlist:
                        haisouryoustr = str(haisouryou)
                        resulthaisouryou = haisouryoustr
                        haisoukaku =  input('間違いないですか？（1:はい　2:いいえ）')
                        if haisoukaku == '1':
                            cus_list[6] = resulthaisouryou
                            break
                        else:
                            print('入力しなおしてください。')
                    else:
                        print('正しいメニュー番号を入力してください。')
            elif henkou == '7':
                mail = input('メールアドレス（半角英数字80文字以内）>')
                mailnum = mail.replace('.','').replace(',','').replace('-','').replace('@','')
                checkmail = len(mail)
                conn = sql_execute()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("USE shopping_cart")
                conn.commit()
                a = "select メールアドレス,ログインID from 顧客一覧"
                cur.execute(a)
                mailkakunin = cur.fetchall()
                conn.commit()
                cur.close()
                conn.close()
                maillist = []
                for i in mailkakunin:
                    for j in i.values():
                        maillist.append(j)
                if mail not in maillist:
                    if "'" in mail or '"' in mail or "’" in mail or '”' in mail:
                        print('入力内容が間違っています。もう一度入力してください。')
                    elif mailnum.encode('utf-8').isalnum() and 1 <= checkmail <= 80:
                        resultmail = mail
                        mailkaku = input('間違いないですか？（1:はい　2:いいえ）')
                        if mailkaku == '1':
                            cus_list[7] = resultmail
                            break
                        else:
                            print('入力しなおしてください。')
                    else:
                        print('入力文字数が間違っています。もう一度入力してください。')
                else:
                    print('このメールアドレスは使用できません')
            elif henkou == '8':
                password = input('パスワード（半角英数字5文字以上10文字以内）>')
                checkpassword = len(password)
                if password.isalnum() and 5 <= checkpassword <= 10:

                    passkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if passkaku == '1':
                        cus_list[9] = password
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数、もしくは形式が間違っています。もう一度入力してください。')
            else:
                print('正しい項目を入力してください。')

        while True:
            saisyu = input('行いたい処理を入力してください。(1:変更する 2:やり直す 3:変更を取りやめてメインメニューに戻る)\n>')
            if saisyu == '1':
                conn = sql_execute()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("USE shopping_cart")
                conn.commit()

                update = "insert into 顧客(名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料管理番号,メールアドレス,ログインID,ログインパスワード)\
                     values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(update,[cus_list[1],cus_list[2],cus_list[3],cus_list[4],cus_list[5],cus_list[6],cus_list[7],cus_list[8],cus_list[9]])
                conn.commit()
                cur.close()
                conn.close()
                print('変更が完了しました。')
                madayaru = input('続けて変更しますか？(1:はい 2:いいえ)')
                if madayaru == '1':
                    break
                elif madayaru == '2':
                    print('メインメニューに戻ります。')
                    stop += 1
                    break
                else:
                    print('正しい数を入力してください')
            elif saisyu == '2':
                print('もう一度入力してください。')
                break
            elif saisyu == '3':
                print('メインメニューに戻ります。')
                stop += 1
                break
            else:
                print('正しい数を入力してください。')
