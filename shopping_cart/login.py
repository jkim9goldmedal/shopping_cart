def login():
    from execute import sql_execute
    import pymysql
    logf = 0
    while logf < 1:
        while True:
            print('ログインを行います。')
            loginid = input('ログインIDを入力してください。（半角英数字5文字以上10文字以内）>')
            loginidcheck = len(loginid)
            if loginid.isalnum() and 5 <= loginidcheck <= 10:
                break
            else:
                print('入力が間違っています。もう一度入力してください。')

        while True:
            loginpass = input('パスワードを入力してください。（半角英数字5文字以上10文字以内）>')
            passcheck = len(loginpass)
            if loginpass.isalnum() and 5 <= passcheck <= 10:
                break
            else:
                print('入力が間違っています。もう一度入力してください。')


        conn = sql_execute()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("USE shopping_cart")
        conn.commit()
        logcus = "select ログインID,ログインパスワード from 【ログイン用】顧客一覧"
        cur.execute(logcus)
        rowslo = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()


        for log in rowslo:
            cus_list = []
            for k in log.values():
                cus_list.append(k)
            if loginid == cus_list[0] and loginpass == cus_list[1]:
                print('ログインに成功しました。ショッピングメニューに移動します。')
                result = cus_list[0]
                logf = logf + 1
                break
        if logf == 0:
            print('ログインIDもしくはパスワードが違います。もう一度入力してください。')
    return result
