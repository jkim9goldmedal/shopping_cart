def cartnull(x):
    from execute import sql_execute
    p = "select count(id) from カート where 顧客ID={} group by 顧客ID".format(x)
    cartcount = sql_execute(p)

    result = cartcount

    return result
