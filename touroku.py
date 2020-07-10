def touroku():
    from execute import sql_execute
    print("記号の「'」と")
    print('「"」は入力できません。\n')
    while True:

        while True:
            name = input('名前（40文字以内）>')
            checkname = len(name)
            if "'" in name or '"' in name:
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
            if "'" in kana or '"' in kana:
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
                if checkzipcode = 7:
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
            if "'" in address or '"' in address:
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
                tel = int(input('電話番号（10-11文字以内）>'))
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                telstr = str(tel)
                checktel = len(telstr)
                if 10 <= checktel <= 11:
                    resulttel = tel
                    telkaku = input('間違いないですか？（1:はい　2:いいえ）')
                    if telkaku == '1':
                        break
                    else:
                        print('入力しなおしてください。')
                else:
                    print('入力文字数が間違っています。もう一度入力してください。')
        while True:
            try:
                cusrank = int(input('優良顧客ですか？(１：はい　２：いいえ)>'))
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                cusrankstr = str(cusrank)
                resultcusrank = cusrankstr
                cusrankkaku = input('間違いないですか？（１：はい　２：いいえ）')
                if cusrankkaku == '1':
                    break
                else:
                    print('入力しなおしてください。')


        while True:
            try:
                haisouryou = int(input('住所に該当する配送料の番号を入力してください。（1:本州、2:離島）>'))
            except ValueError as ve:
                print('数字以外を入力しています。もう一度入力してください。')
            else:
                haisouryoustr = str(haisouryou)
                resulthaisouryou = haisouryoustr
                haisoukaku =  input('間違いないですか？（1:はい　2:いいえ）')
                if haisoukaku == '1':
                    break
                else:
                    print('入力しなおしてください。')

        while True:
            mail = input('メールアドレス（半角英数字80文字以内）>')
            checkmail = len(mail)
            if "'" in address or '"' in address:
                print('入力内容が間違っています。もう一度入力してください。')
            elif mail.encode('utf-8').isalnum() and 1 <= checkmail <= 50:
                resultmail = mail
                mailkaku = input('間違いないですか？（1:はい　2:いいえ）')
                if mailkaku == '1':
                    break
                else:
                    print('入力しなおしてください。')
            else:
                print('入力文字数が間違っています。もう一度入力してください。')

        while True:
            password = input('パスワード（半角英数字5文字以上10文字以内）>')
            checkpassword = len(password)
            if password.encode('utf-8').isalnum() and 5 <= checkpassword <= 10:
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
        return resultname,resultkana,resultzipcode,resultaddress,resulttel,resultcusrank,resulthaisouryou,resultmail,resultpassword
    elif saisyu == '2'
        print('もう一度入力してください。')
    else:
        print('正しい数を入力してください。')
