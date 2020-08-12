def data_rireki(zyutyuid):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    b = "select 受注明細.商品番号,受注ID,商品名,商品詳細,税込金額,税抜金額,数量,受注明細.販売単価,受注明細.税込販売単価\
        from 受注明細 inner join 商品在庫一覧 on 受注明細.商品番号 = 商品在庫一覧.商品番号\
        where 受注ID = %s"
    cur.execute(b,zyutyuid)
    zyutyu_meisai = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    data = []
    for i in zyutyu_meisai:
        column_list = []
        itemcode,zyutyu_id,name,namedet,taxprice,price,num,genka,taxgenka = i.values()
        num = str(num) + '個'
        taxprice = str(taxprice) + '円'
        price = '(' + str(price) + '円)'

        column_list = [itemcode,name,namedet,taxprice,price,num]

        data.append(column_list)

    return data
