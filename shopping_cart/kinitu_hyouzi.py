def kinitu_hyouzi(item_list):
    import pymysql
    from execute import sql_execute
    item_list[10]
    item_list[10] = round(item_list[10])
    print('【セール】')
    print(item_list[1],end = '/')
    print(item_list[2],end = '/')
    print(item_list[3],end = '/')
    print('{:,}'.format(item_list[10]) + '円',end = '/')
    # print('{:,}'.format(item_list[11]) + '円',end = '')
    print()
    print('\n')
