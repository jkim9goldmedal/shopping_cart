def hyouzi(x):
    from execute import sql_execute
    print('1:登録内容表示・変更\n')
    print('登録内容を表示します。')

    a = "select 名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインパスワード\
        from customers\
        where id = {}".format(x)

    rows = sql_execute(a)
    for row in rows:
        print('名前:' + row[0])
        print('カナ:' + row[1])
        print('郵便番号:' + row[2])
        print('住所:' + row[3])
        print('電話番号:' + row[4])
        print('顧客ランク（1:普通　2:有料会員）:' + row[5])
        print('配送料ID（1:本州 2:離島）:' + row[6])
        print('メールアドレス:' + row[7])
        print('ログインパスワード' + row[8])
        print()
