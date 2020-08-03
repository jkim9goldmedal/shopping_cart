def itemdis_hyouzi(item_list):
    item_list[5]
    item_list[5] = round(item_list[5])
    print('【セール】')
    print(item_list[0],end = '/')
    print(item_list[1],end = '/')
    print(item_list[2],end = '/')
    print('{:,}'.format(item_list[5]) + '円',end = '/')
    # print('{:,}'.format(item_list[7]) + '円',end = '')
    print()
    print('\n')
