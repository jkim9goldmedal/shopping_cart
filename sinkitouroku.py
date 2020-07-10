def sinkitouroku():
    from execute import sql_execute
    from touroku import touroku

    print('登録内容を入力してください。')

    result = touroku()

    cus = "insert into customers(名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインパスワード)　values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])
    sql_execute(cus)


    print('あなたのログインIDはメールアドレスです。\nログイン時にパスワードと両方必要なのでメモ等で控えておいてください。')
