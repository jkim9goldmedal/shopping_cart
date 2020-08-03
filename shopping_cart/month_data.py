def data_month():
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    # a = "select 受注日,商品番号,商品名,商品詳細,sum(case when DATE_FORMAT(受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m') then 数量 else 0 end),sum(case when DATE_FORMAT(受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m') then 税込金額 else 0 end),sum(case when DATE_FORMAT(受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m') then 税抜金額 else 0 end),税込販売単価,受注明細.販売単価,受注.削除フラグ,受注明細.削除フラグ\
    #     from 受注明細 inner join 受注 on 受注ID = 受注.id inner join 商品 on 受注明細.商品番号 = 商品.商品番号\
    #     group by 商品名\
    #     having 受注.削除フラグ = 0 and 受注明細.削除フラグ = 0 and DATE_FORMAT(受注日,'%Y/%m') = DATE_FORMAT(now(),'%Y/%m')"
    a = "select A.受注日,A.商品番号,A.商品名,A.商品詳細,A.販売単価,sum(A.数量) as 数量,sum(A.税抜金額) as 税抜金額,sum(A.税込金額) as 税込金額\
        from 受注明細情報一覧 A\
        where exists(\
            select *\
            from 受注明細情報一覧 B\
            where A.商品番号 = B.商品番号 and A.販売単価 = B.販売単価 and DATE_FORMAT(B.受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m'))\
            and DATE_FORMAT(A.受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')\
        group by A.商品番号, A.販売単価\
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
        sumprice = str(sumprice) + '円'
        price = str(price) + '円'
        column_list = [itemcode,name,namedet,price,sumnum,sumprice,sumtaxprice]

        data.append(column_list)

    return data
