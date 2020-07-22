def search_null_id(result):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()

    c = "select count(商品.id),在庫.商品ID,商品番号,商品名,商品詳細,round(販売単価*(1+(税率/100))),販売単価,round(販売単価*(1-(商品割引率/100))*(1+(税率/100))),round(販売単価*(1-(商品割引率/100))),round(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100))),round(販売単価*(1-(カテゴリー割引率/100))),round(均一単価*(1+(税率/100))),均一単価,sum(在庫変動数),割引フラグ,商品.削除フラグ,商品カテゴリーID\
        from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
        group by 在庫.商品ID\
        having 商品.削除フラグ = 0 and 商品カテゴリーID = %s and sum(在庫変動数) > 0"
    cur.execute(c,result)
    rows3 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    if rows3 == ():
        print('該当商品はありませんでした。')
    else:
        print('商品が見つかりました。')
