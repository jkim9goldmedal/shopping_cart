def cartdel(x):
    from execute import sql_execute
    cartdel = "delete from cart where 顧客ID ={}".format(x)
    sql_execute(cartdel)
