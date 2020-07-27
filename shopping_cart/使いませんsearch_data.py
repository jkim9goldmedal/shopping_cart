def search_data(result):
    import pymysql
    from execute import sql_execute
    conn = sql_execute()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("USE shopping_cart")
    conn.commit()
    b = "select 在庫.商品ID,商品番号,商品名,商品詳細,round(販売単価*(1+(税率/100))),販売単価,round(販売単価*(1-(商品割引率/100))*(1+(税率/100))),round(販売単価*(1-(商品割引率/100))),round(販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100))),round(販売単価*(1-(カテゴリー割引率/100))),round(均一単価*(1+(税率/100))),均一単価,sum(在庫変動数),割引フラグ,商品.削除フラグ,商品カテゴリーID\
        from 在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
        group by 在庫.商品ID\
        having 商品.削除フラグ = 0 and 商品カテゴリーID = %s and sum(在庫変動数) > 0"


    cur.execute(b,result)
    rows2 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    data = []
    for k in rows2:
        item_list = []
        id,itemcode,name,namedet,taxprice,price,itemdistax,itemdis,categorydistax,categorydis,kinitutax,kinitu,zaiko,disflag,delflag,kategoryid = k.values()
        sale = ''
        taxprice = str(taxprice) + '円'
        price = str(price) + '円'
        itemdistax = str(itemdistax) + '円'
        itemdis = str(itemdis) + '円'
        categorydistax = str(categorydistax) + '円'
        categorydis = str(categorydis) + '円'
        kinitutax = str(kinitutax) + '円'
        kinitu = str(kinitu) + '円'
        item_list = [sale,itemcode,name,namedet,taxprice,price]
        data.append(item_list)
    return data
