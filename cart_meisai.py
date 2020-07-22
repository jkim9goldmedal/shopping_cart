def cart_meisai(x):
    from execute import sql_execute
    import pymysql
    import cart_column
    column = cart_column.column()
    import cart_data
    data = cart_data.data_cart(x)
    import item_info
    item_info.item_info(data,column)
    print('=====================')
    import cart_keisan
    keisan = cart_keisan.keisan(x)
    print('税込商品合計(税抜商品合計)',end = '')
    print(':'.rjust(5),end = '')
    print('{:,}'.format(keisan[0]).rjust(13),end = '')
    print('円(',end = '')
    print('{:,}'.format(keisan[1]).rjust(6),end = '')
    print('円)')
    print('税込配送料(税抜配送料)',end = '')
    print(':'.rjust(9),end = '')
    print('{:,}'.format(keisan[3]).rjust(13),end = '')
    print('円(',end = '')
    print('{:,}'.format(keisan[2]).rjust(6),end = '')
    print('円)')
    print('総額',end = '')
    print(':'.rjust(27),end = '')
    print('{:,}'.format(keisan[4]).rjust(13),end = '')
    print('円')
    print('====================')
    print('振込先情報\nvv銀行\n赤坂支店\n口座番号:1234567\n名義：カトウアツシ')
