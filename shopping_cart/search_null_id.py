def search_null_id(result):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()

    c = "select count(商品番号)\
        from 商品在庫一覧\
        where 商品カテゴリー番号 = %s and 在庫数 > 0 and 削除フラグ = 0"
    cur.execute(c,result)
    rows3 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    idlist = []
    for i in rows3:
        for j in i.values():
            idlist.append(j)

    if idlist == [0]:
        print('該当商品はありませんでした。')
    else:
        print('商品が見つかりました。')
