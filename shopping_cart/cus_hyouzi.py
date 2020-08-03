def hyouzi(x):
    import pymysql
    from execute import sql_execute
    print('1:登録内容表示・変更\n')
    print('登録内容を表示します。')

    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select 名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインID,ログインパスワード\
        from 【ログイン用】顧客一覧\
        where ログインID = %s"

    cur.execute(a,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    for row in rows:
        cus_list = []
        for r in row.values():
            cus_list.append(r)

        print('名前:' + cus_list[0])
        print('カナ:' + cus_list[1])
        print('郵便番号:' + cus_list[2])
        print('住所:' + cus_list[3])
        print('電話番号:' + cus_list[4])
        print('顧客ランク（1:有料会員　2:普通会員）:' + cus_list[5])
        print('配送料ID（1:本州 2:離島）:' + str(cus_list[6]))
        print('メールアドレス:' + cus_list[7])
        print('ログインID(変更不可):' + cus_list[8])
        print('ログインパスワード:' + cus_list[9])
        print()
