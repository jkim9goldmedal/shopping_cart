def categorydis_hyouzi(item_list):
    item_list[7]
    item_list[7] = round(item_list[7])
    #カテゴリー割引率
    print('【セール】',end = '/')
    print(item_list[0],end = '/')
    print(item_list[1],end = '/')
    print(item_list[2],end = '/')
    print('{:,}'.format(item_list[7]) + '円',end = '/')
    # print('{:,}'.format(item_list[9]) + '円',end = '')
    print()
    print('\n')
