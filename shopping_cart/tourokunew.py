def tourokunew():
    from execute import sql_execute
    import pymysql
    print("記号の「'」と")
    print('「"」は入力できません。\n')
    print('メニューに戻りたいときは「0」を入力してください。')
    tourokuf = 0
    while tourokuf < 1:
        namef =0
        while namef < 1:
            name = input('名前（40文字以内）>')
            checkname = len(name)
            if "'" in name or '"' in name or "’" in name or '”' in name:
                print('入力内容が間違っています。もう一度入力してください。')
            elif name == '0':
                namef += 1
                tourokuf += 1

            elif 1 <= checkname <= 40:
                resultname = name
                namekaku = input('間違いないですか？（1:はい　2:いいえ）>')
                if namekaku == '1':
                    kanaf = 0
                    while kanaf < 1:
                        kana = input('カナ（40文字以内）>')
                        checkkana = len(kana)
                        if "'" in kana or '"' in kana or "’" in kana or '”' in kana:
                            print('入力内容が間違っています。もう一度入力してください。')
                        elif kana == '0':
                            kanaf += 1
                            namef += 1
                            tourokuf += 1
                        elif 1 <= checkkana <= 40:
                            resultkana = kana
                            kanakaku = input('間違いないですか？（1:はい　2:いいえ）>')
                            if kanakaku == '1':
                                zipf = 0
                                while zipf < 1:
                                    try:
                                        zipcode = int(input('郵便番号（7桁）>'))
                                    except ValueError as ve:
                                        print('数字以外を入力しています。もう一度入力してください。')
                                    else:
                                        zipcodestr = str(zipcode)
                                        checkzipcode = len(zipcodestr)
                                        if zipcode == 0:
                                            zipf += 1
                                            kanaf += 1
                                            namef += 1
                                            tourokuf += 1
                                        elif checkzipcode == 7:
                                            resultzipcode = zipcode
                                            zipkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                            if zipkaku == '1':
                                                addressf = 0
                                                while addressf < 1:
                                                    address = input('住所（100文字以内）>')
                                                    checkaddress = len(address)
                                                    if "'" in address or '"' in address or "’" in address or '”' in address:
                                                        print('入力内容が間違っています。もう一度入力してください。')
                                                    elif address == '0':
                                                        addressf += 1
                                                        zipf += 1
                                                        kanaf += 1
                                                        namef += 1
                                                        tourokuf += 1
                                                    elif 1 <= checkaddress <= 100:
                                                        resultaddress = address
                                                        addkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                                        if addkaku == '1':
                                                            telf = 0
                                                            while telf < 1:
                                                                try:
                                                                    tel = int(input('電話番号（10-11文字以内,最初の「0」は除いて入力してください。\n例:09012345678→9012345678）\n>'))
                                                                    tel1 = '0' + str(tel)
                                                                except ValueError as ve:
                                                                    print('数字以外を入力しています。もう一度入力してください。')
                                                                else:
                                                                    telstr = str(tel)
                                                                    checktel = len(telstr)
                                                                    if tel == 0:
                                                                        telf += 1
                                                                        addressf += 1
                                                                        zipf += 1
                                                                        kanaf += 1
                                                                        namef += 1
                                                                        tourokuf += 1
                                                                    elif 9 <= checktel <= 10:
                                                                        resulttel = tel1
                                                                        telkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                                                        if telkaku == '1':
                                                                            cusrankf = 0
                                                                            while cusrankf < 1:
                                                                                try:
                                                                                    cusrank = int(input('優良顧客ですか？(1:はい　2:いいえ)>'))
                                                                                except ValueError as ve:
                                                                                    print('数字以外を入力しています。もう一度入力してください。')
                                                                                else:
                                                                                    if cusrank == 0:
                                                                                        cusrankf += 1
                                                                                        telf += 1
                                                                                        addressf += 1
                                                                                        zipf += 1
                                                                                        kanaf += 1
                                                                                        namef += 1
                                                                                        tourokuf += 1
                                                                                    if cusrank == 1 or cusrank == 2:
                                                                                        cusrankstr = str(cusrank)
                                                                                        resultcusrank = cusrankstr
                                                                                        cusrankkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                                                                        if cusrankkaku == '1':
                                                                                            haisouf = 0
                                                                                            while haisouf < 1:
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
                                                                                                    if haisouryou == 0:
                                                                                                        haisouf += 1
                                                                                                        cusrankf += 1
                                                                                                        telf += 1
                                                                                                        addressf += 1
                                                                                                        zipf += 1
                                                                                                        kanaf += 1
                                                                                                        namef += 1
                                                                                                        tourokuf += 1
                                                                                                    elif haisouryou in hhlist:

                                                                                                        haisouryoustr = str(haisouryou)
                                                                                                        resulthaisouryou = haisouryoustr
                                                                                                        haisoukaku =  input('間違いないですか？（1:はい　2:いいえ）>')
                                                                                                        if haisoukaku == '1':
                                                                                                            mailf = 0
                                                                                                            while mailf < 1:
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
                                                                                                                if mail == '0':
                                                                                                                    mailf += 1
                                                                                                                    haisouf += 1
                                                                                                                    cusrankf += 1
                                                                                                                    telf += 1
                                                                                                                    addressf += 1
                                                                                                                    zipf += 1
                                                                                                                    kanaf += 1
                                                                                                                    namef += 1
                                                                                                                    tourokuf += 1
                                                                                                                elif mail not in maillist:
                                                                                                                    if "'" in mail or '"' in mail or "’" in mail or '”' in mail:
                                                                                                                        print('入力内容が間違っています。もう一度入力してください。')
                                                                                                                    elif mailnum.encode('utf-8').isalnum() and 1 <= checkmail <= 80:
                                                                                                                        resultmail = mail
                                                                                                                        mailkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                                                                                                        if mailkaku == '1':
                                                                                                                            loginidf = 0
                                                                                                                            while loginidf < 1:
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
                                                                                                                                if loginid == '0':
                                                                                                                                    loginidf += 1
                                                                                                                                    mailf += 1
                                                                                                                                    haisouf += 1
                                                                                                                                    cusrankf += 1
                                                                                                                                    telf += 1
                                                                                                                                    addressf += 1
                                                                                                                                    zipf += 1
                                                                                                                                    kanaf += 1
                                                                                                                                    namef += 1
                                                                                                                                    tourokuf += 1

                                                                                                                                elif loginid not in loginidlist:
                                                                                                                                    if loginid.encode('utf-8').isalnum() and 5 <= checkloginid <= 10:
                                                                                                                                        resultloginid = loginid
                                                                                                                                        logidkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                                                                                                                        if logidkaku == '1':
                                                                                                                                            passf = 0
                                                                                                                                            while passf < 1:
                                                                                                                                                password = input('パスワード（半角英数字5文字以上10文字以内）>')
                                                                                                                                                checkpassword = len(password)
                                                                                                                                                if password == '0':
                                                                                                                                                    passf += 1
                                                                                                                                                    loginidf += 1
                                                                                                                                                    mailf += 1
                                                                                                                                                    haisouf += 1
                                                                                                                                                    cusrankf += 1
                                                                                                                                                    telf += 1
                                                                                                                                                    addressf += 1
                                                                                                                                                    zipf += 1
                                                                                                                                                    kanaf += 1
                                                                                                                                                    namef += 1
                                                                                                                                                    tourokuf += 1
                                                                                                                                                elif password.isalnum() and 5 <= checkpassword <= 10:
                                                                                                                                                    resultpassword = password
                                                                                                                                                    passkaku = input('間違いないですか？（1:はい　2:いいえ）>')
                                                                                                                                                    if passkaku == '1':
                                                                                                                                                        saisyuf = 0
                                                                                                                                                        while saisyuf < 1:
                                                                                                                                                            saisyu = input('登録しますか？（1:はい　2:いいえ）>')
                                                                                                                                                            if saisyu == '1':
                                                                                                                                                                result = resultname,resultkana,resultzipcode,resultaddress,resulttel,resultcusrank,resulthaisouryou,resultmail,resultloginid,resultpassword
                                                                                                                                                                conn = sql_execute()
                                                                                                                                                                cur = conn.cursor(pymysql.cursors.DictCursor)
                                                                                                                                                                cur.execute("USE shopping_cart")
                                                                                                                                                                conn.commit()
                                                                                                                                                                cus = "insert into 顧客(名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料管理番号,メールアドレス,ログインID,ログインパスワード) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


                                                                                                                                                                cur.execute(cus,result)
                                                                                                                                                                conn.commit()
                                                                                                                                                                cur.close()
                                                                                                                                                                conn.close()


                                                                                                                                                                print('登録が完了しました。\nログイン時にログインIDとパスワードが両方必要なのでメモ等で控えておいてください。')
                                                                                                                                                                saisyuf += 1


                                                                                                                                                                passf += 1
                                                                                                                                                                loginidf += 1
                                                                                                                                                                mailf += 1
                                                                                                                                                                haisouf += 1
                                                                                                                                                                cusrankf += 1
                                                                                                                                                                telf += 1
                                                                                                                                                                addressf += 1
                                                                                                                                                                zipf += 1
                                                                                                                                                                kanaf += 1
                                                                                                                                                                namef += 1
                                                                                                                                                                tourokuf += 1

                                                                                                                                                            elif saisyu == '2':
                                                                                                                                                                print('もう一度入力してください。')
                                                                                                                                                                saisyuf += 1
                                                                                                                                                                passf += 1
                                                                                                                                                                loginidf += 1
                                                                                                                                                                mailf += 1
                                                                                                                                                                haisouf += 1
                                                                                                                                                                cusrankf += 1
                                                                                                                                                                telf += 1
                                                                                                                                                                addressf += 1
                                                                                                                                                                zipf += 1
                                                                                                                                                                kanaf += 1
                                                                                                                                                                namef += 1

                                                                                                                                                            else:
                                                                                                                                                                print('正しい数を入力してください。')
                                                                                                                                                    else:
                                                                                                                                                        print('入力しなおしてください。')
                                                                                                                                                else:
                                                                                                                                                    print('入力文字数が間違っています。もう一度入力してください。')
                                                                                                                                        else:
                                                                                                                                            print('入力しなおしてください。')
                                                                                                                                    else:
                                                                                                                                        print('入力文字数が間違っています。もう一度入力してください。')
                                                                                                                                else:
                                                                                                                                    print('このログインIDは使用できません。')
                                                                                                                        else:
                                                                                                                            print('入力しなおしてください。')
                                                                                                                    else:
                                                                                                                        print('入力文字数が間違っています。もう一度入力してください。')
                                                                                                                else:
                                                                                                                    print('このメールアドレスは使用できません')
                                                                                                        else:
                                                                                                            print('入力しなおしてください。')
                                                                                                    else:
                                                                                                        print('正しいメニュー番号を入力してください。')
                                                                                        else:
                                                                                            print('入力しなおしてください。')
                                                                                    else:
                                                                                        print('正しいメニュー番号を入力してください。')
                                                                        else:
                                                                            print('入力しなおしてください。')
                                                                    else:
                                                                        print('入力文字数が間違っています。もう一度入力してください。')
                                                        else:
                                                            print('入力しなおしてください。')
                                                    else:
                                                        print('入力文字数が間違っています。もう一度入力してください。')
                                            else:
                                                print('入力しなおしてください。')
                                        else:
                                            print('入力文字数が間違っています。もう一度入力してください。')
                            else:
                                print('入力しなおしてください。')
                        else:
                            print('入力文字数が間違っています。もう一度入力してください。')
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')
