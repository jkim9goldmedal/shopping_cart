def sinkitouroku():
    import pymysql
    from execute import sql_execute
    from touroku import touroku

    print('登録内容を入力してください。')

    result = touroku()

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
