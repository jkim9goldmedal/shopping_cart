def itemdis_hyouzi(item_list):
    item_list[6]
    item_list[6] = round(item_list[6])
    print('【セール】')
    print(item_list[1],end = '/')
    print(item_list[2],end = '/')
    print(item_list[3],end = '/')
    print('{:,}'.format(item_list[6]) + '円',end = '/')
    # print('{:,}'.format(item_list[7]) + '円',end = '')
    print()
    print('\n')
