def touroku():
    from execute import sql_execute
    import pymysql
    print("記号の「'」と")
    print('「"」は入力できません。\n')
    tourokuf = 0
    while tourokuf < 1:

        while True:
            name = input('名前（40文字以内）>')
            checkname = len(name)
            if "'" in name or '"' in name or "’" in name or '”' in name:
                print('入力内容が間違っています。もう一度入力してください。')
            elif 1 <= checkname <= 40:
                resultname = name
                namekaku = input('間違いないですか？（1:はい　2:いいえ）')
                if namekaku == '1':
                    break
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')

        while True:
            kana = input('カナ（40文字以内）>')
            checkkana = len(kana)
            if "'" in kana or '"' in kana or "’" in kana or '”' in kana:
                print('入力内容が間違っています。もう一度入力してください。')
            elif 1 <= checkkana <= 40:
                resultkana = kana
                kanakaku = input('間違いないですか？（1:はい　2:いいえ）')
                if kanakaku == '1':
                    break
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')

        while True:
            try:
                zipcode = int(input('郵便番号（7桁）>'))
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                zipcodestr = str(zipcode)
                checkzipcode = len(zipcodestr)
                if checkzipcode == 7:
                    resultzipcode = zipcode
                    zipkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if zipkaku == '1':
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数が間違っています。もう一度入力してください。')

        while True:
            address = input('住所（100文字以内）>')
            checkaddress = len(address)
            if "'" in address or '"' in address or "’" in address or '”' in address:
                print('入力内容が間違っています。もう一度入力してください。')
            elif 1 <= checkaddress <= 100:
                resultaddress = address
                addkaku = input('間違いないですか？（1:はい　2:いいえ）')
                if addkaku == '1':
                    break
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')

        while True:
            try:
                tel = int(input('電話番号（10-11文字以内,最初の「0」は除いて入力してください。\n例:09012345678→9012345678）\n>'))
                tel1 = '0' + str(tel)
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                telstr = str(tel)
                checktel = len(telstr)
                if 9 <= checktel <= 10:
                    resulttel = tel1
                    telkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if telkaku == '1':
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数が間違っています。もう一度入力してください。')
        while True:
            try:
                cusrank = int(input('優良顧客ですか？(1:はい　2:いいえ)>'))
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                if cusrank == 1 or cusrank == 2:
                    cusrankstr = str(cusrank)
                    resultcusrank = cusrankstr
                    cusrankkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if cusrankkaku == '1':
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('正しいメニュー番号を入力してください。')


        while True:
            try:
                haisouryou = int(input('住所に該当する配送料の番号を入力してください。（1:本州、2:離島）>'))
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                if haisouryou == 1 or haisouryou == 2:

                    haisouryoustr = str(haisouryou)
                    resulthaisouryou = haisouryoustr
                    haisoukaku =  input('間違いないですか？（1:はい　2:いいえ）')
                    if haisoukaku == '1':
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('正しいメニュー番号を入力してください。')

        while True:
            mail = input('メールアドレス（半角英数字80文字以内）>')
            mailnum = mail.replace('.','').replace(',','').replace('-','').replace('@','')
            checkmail = len(mail)
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            a = "select メールアドレス,id from 顧客 where 削除フラグ = 0"
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
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数が間違っています。もう一度入力してください。')
            else:
                print('このメールアドレスは使用できません')

        while True:
            loginid = input('ログインID（半角英数字5文字以上10文字以内。後からの変更はできません。）>')
            checkloginid = len(loginid)
            conn = sql_execute()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("USE shopping_cart")
            conn.commit()
            a = "select ログインID,id from 顧客 where 削除フラグ = 0"
            cur.execute(a)
            loginidkakunin = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            loginidlist = []
            for i in loginidkakunin:
                for j in i.values():
                    loginidlist.append(j)
            if loginid.encode('utf-8').isalnum() and 5 <= checkloginid <= 10:
                resultloginid = loginid
                logidkaku = input('間違いないですか？（1:はい　2:いいえ）')
                if logidkaku == '1':
                    break
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')


        while True:
            password = input('パスワード（半角英数字5文字以上10文字以内）>')
            checkpassword = len(password)
            if password.isalnum() and 5 <= checkpassword <= 10:
                resultpassword = password
                passkaku = input('間違いないですか？（1:はい　2:いいえ）')
                if passkaku == '1':
                    break
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')


        saisyu = input('登録しますか？（1:はい　2:いいえ）')
        if saisyu == '1':
            return resultname,resultkana,resultzipcode,resultaddress,resulttel,resultcusrank,resulthaisouryou,resultmail,resultloginid,resultpassword
            tourokuf = tourokuf + 1
        elif saisyu == '2':
            print('もう一度入力してください。')
        else:
            print('正しい数を入力してください。')
