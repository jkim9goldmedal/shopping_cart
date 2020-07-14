def henkou(x):
    from execute import sql_execute
    import pymysql
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select 名前,カナ,郵便番号,住所,電話番号,顧客ランク,配送料ID,メールアドレス,ログインパスワード\
        from 顧客\
        where id = %s"

    cur.execute(a,x)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
