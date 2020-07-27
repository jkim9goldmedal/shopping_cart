def henkou(x):
    from execute import sql_execute
    import pymysql
    stop = 0
    while stop < 1:

        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        a = "select id,名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインパスワード\
            from 顧客\
            where id = %s"

        cur.execute(a,x)
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        print('変更を行います。')

        for i in rows:
            cus_list = []
            for j in i.values():
                cus_list.append(j)
        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        cus = "insert into 顧客(名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインパスワード,削除フラグ,備考)\
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,1,cast(now()as date))"
        cur.execute(cus,[cus_list[1],cus_list[2],cus_list[3],cus_list[4],cus_list[5],cus_list[6],cus_list[7],cus_list[8],cus_list[9]])
        conn.commit()
        cur.close()
        conn.close()

        # henkou = input('変更したい項目を入力してください。>')
        # henkounaiyou = input('変更後の内容を入力してください。>')

        while True:
            henkou = input('変更したい項目を入力してください。>')
            if henkou == '名前':
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
            elif henkou == 'カナ':
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
            elif henkou == '郵便番号':
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
            elif henkou == '住所':
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
            elif henkou == '電話番号':
                try:
                    tel = int(input('電話番号（10-11文字以内）>'))
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
            elif henkou == '顧客ランク':
                try:
                    cusrank = int(input('優良顧客ですか？(1:はい　2:いいえ)>'))
                except ValueError as ve:
                    print('数字以外を入力しています。もう一度入力してください。')
                else:
                    cusrankstr = str(cusrank)
                    resultcusrank = cusrankstr
                    cusrankkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if cusrankkaku == '1':
                        cus_list[6] = resultcusrank
                        break
                    else:
                        print('入力しなおしてください。')
            elif henkou == '配送料ID':
                try:
                    haisouryou = int(input('住所に該当する配送料の番号を入力してください。（1:本州、2:離島）>'))
                except ValueError as ve:
                    print('数字以外を入力しています。もう一度入力してください。')
                else:
                    haisouryoustr = str(haisouryou)
                    resulthaisouryou = haisouryoustr
                    haisoukaku =  input('間違いないですか？（1:はい　2:いいえ）')
                    if haisoukaku == '1':
                        cus_list[7] = resulthaisouryou
                        break
                    else:
                        print('入力しなおしてください。')
            elif henkou == 'メールアドレス':
                mail = input('メールアドレス（半角英数字80文字以内）>')
                checkmail = len(mail)
                if "'" in mail or '"' in mail or "’" in mail or '”' in mail:
                    print('入力内容が間違っています。もう一度入力してください。')
                elif mail.isalnum() and 1 <= checkmail <= 80:

                    mailkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if mailkaku == '1':
                        cus_list[8] = mail
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数、もしくは形式が間違っています。もう一度入力してください。')
            elif henkou == 'ログインパスワード':
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
        saisyu = input('行いたい処理を入力してください。(1:変更する 2:やり直す 3:変更を取りやめてメインメニューに戻る)')
        if saisyu == '1':
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()

            update = "update 顧客\
                set 名前 = %s,カナ = %s,郵便番号 = %s,住所 = %s,電話番号 = %s,顧客ランク = %s,配送料ID = %s,メールアドレス = %s,ログインパスワード = %s\
                where id = %s"
            cur.execute(update,[cus_list[1],cus_list[2],cus_list[3],cus_list[4],cus_list[5],cus_list[6],cus_list[7],cus_list[8],cus_list[9],x])
            conn.commit()
            cur.close()
            conn.close()
            print('変更が完了しました。')
            stop += 1
        elif saisyu == '2':
            print('もう一度入力してください。')
        elif saisyu == '3':
            print('メインメニューに戻ります。')
            stop += 1
        else:
            print('正しい数を入力してください。')
