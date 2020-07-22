def data():
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select 受注日,商品番号,商品名,商品詳細,sum(case when 受注日 = cast(now() as date) then 数量 else 0 end),sum(case when 受注日 = cast(now() as date) then 税込金額 else 0 end),sum(case when 受注日 = cast(now() as date) then 税抜金額 else 0 end),税込販売単価,受注明細.販売単価,受注.削除フラグ,受注明細.削除フラグ\
        from 受注明細 inner join 受注 on 受注ID = 受注.id inner join 商品 on 商品ID = 商品.id\
        group by 商品名\
        having 受注.削除フラグ = 0 and 受注明細.削除フラグ = 0 and 受注日 = cast(now() as date)"
    cur.execute(a)
    goukeiigai = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    data = []
    for i in goukeiigai:
        column_list = []
        date,itemcode,name,namedet,sumnum,sumtaxprice,sumprice,taxprice,price,saku1,saku2 = i.values()
        sumnum = str(sumnum) + '個'
        sumtaxprice = str(sumtaxprice) + '円'
        sumprice = '(' + str(sumprice) + '円)'
        taxprice = str(taxprice) + '円'
        price = '(' + str(price) + '円)'
        column_list = [itemcode,name,namedet,taxprice,price,sumnum,sumtaxprice,sumprice]

        data.append(column_list)

    return data
