def login():
    from execute import sql_execute
    logf = 0
    while logf < 1:
        while True:
            print('ログインを行います。')
            loginid = input('メールアドレスを入力してください。（半角英数字）>')
            loginidcheck = len (loginid)
            if 1 <= loginidcheck <= 80:
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

        logcus = "select (メールアドレス,ログインパスワード,id) from customers"
        rowslo = sql_execute(logcus)

        sum3 = 0
        for log in rowslo:
            if loginid == log[0] and loginpass == log[1]:
                sum3 = sum3 + 1
                print('ログインに成功しました。ショッピングメニューに移動します。')
                result = log[2]
                logf = logf + 1
                break
        if sum3 == 0:
            print('ログインIDもしくはパスワードが違います。もう一度入力してください。')
    return result
