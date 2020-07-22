def categorydis_hyouzi(item_list):
    item_list[8]
    item_list[8] = round(item_list[8])
    #カテゴリー割引率
    print('【セール】')
    print(item_list[1],end = '/')
    print(item_list[2],end = '/')
    print(item_list[3],end = '/')
    print('{:,}'.format(item_list[8]) + '円',end = '/')
    # print('{:,}'.format(item_list[9]) + '円',end = '')
    print()
    print('\n')
