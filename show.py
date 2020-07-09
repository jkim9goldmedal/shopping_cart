def show():
    from execute import sql_execute
    c = "select 商品.id,商品番号,商品名,商品詳細,TRUNCATE(販売単価*(1+(税率/100)),0),販売単価,TRUNCATE(販売単価*(1-(割引率/100))*(1+(税率/100)),0),TRUNCATE(均一価格*(1+(税率/100)),0),均一単価,在庫数,セールフラグ,均一フラグ,削除フラグ\
        from 商品 inner join 商品カテゴリー on 商品カテゴリーID = 書品カテゴリー.id inner join 税率 on 税率ID = 税率.id\
        inner join 商品カテゴリー on 商品割引率ID = 商品割引率.id \
        where 在庫数 > 0, 削除フラグ = 0\
        group by 商品.id"
    
    a = "select id,カテゴリー from 商品カテゴリー where 削除フラグ = 0"
    
    rows = sql_execute(a)
    
    
    print('2:商品情報検索・一覧')
    print('カテゴリーID:カテゴリー名')
    print(")
    print('カテゴリーを表示します。')
    for i in rows:
          
    
