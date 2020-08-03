def data():
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    a = "select A.受注日,A.商品番号,A.商品名,A.商品詳細,A.販売単価,sum(A.数量) as 数量,sum(A.税抜金額) as 税抜金額,sum(A.税込金額) as 税込金額\
        from 受注明細情報一覧 A\
        where exists(\
            select *\
            from 受注明細情報一覧 B\
            where A.商品番号 = B.商品番号 and A.販売単価 = B.販売単価 and A.受注日 = cast(now() as date))\
        group by A.商品番号,A.販売単価\
        order by A.商品番号"
    cur.execute(a)
    goukeiigai = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    data = []
    for i in goukeiigai:
        column_list = []
        date,itemcode,name,namedet,price,sumnum,sumprice,sumtaxprice = i.values()
        sumnum = str(sumnum) + '個'
        sumtaxprice = str(sumtaxprice) + '円'
        sumprice = '(' + str(sumprice) + '円)'
        price = '(' + str(price) + '円)'
        column_list = [itemcode,name,namedet,price,sumnum,sumprice,sumtaxprice]

        data.append(column_list)

    return data
