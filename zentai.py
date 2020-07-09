def shopping_cart():
    while True:
        print('メニュー\n1:新規登録\n2:ショッピングカートにログイン\n3:お問い合わせ\n4:終了')
        menu = input('行いたい処理のメニュー番号を入力してください。（半角数字）>')
        if menu == '1':
            print('')
            sinkitouroku()
            print('')

        elif menu == '2':
            print('')
            x = login()
            while True:
                print('')

        elif menu == '3':
            print('')

        elif menu == '4':
            print('')
            print('終了します。')
            break

        else:
            print('')
            print('入力内容が間違っています。もう一度入力してください。')
            print('')
