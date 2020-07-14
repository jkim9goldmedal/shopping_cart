def sql_execute():
    import pymysql
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
    return conn
    #カーソル取得
    # cur = conn.cursor(pymysql.cursors.DictCursor)
    #
    # #SQL実行
    # cur.execute(sql)
    #
    # result = cur.fetchall()
    #
    # cur.close()
    # conn.commmit()
    # conn.close()
    #
    # return result
