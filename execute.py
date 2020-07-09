def sql_execute(sql):
    import pymysql.cursors
    #mysqlインポート
    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

    conn = pymysql.connect(
    user = "root",
    passwd = "seigo2017",
    host = "localhost",
    db = "shopping_cart"
    )

    #カーソル取得
    cur = conn.cursor(pymysql.cursors.DictCursor)

    #SQL実行
    cur.execute(sql)

    result = cur.fetchall()

    cur.close()
    conn.commmit()
    conn.close()

    return result
