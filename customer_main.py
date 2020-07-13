from cartnull import cartnull
from sinkitouroku import sinkitouroku
from login import login
from search_show import search_show
from add_cart import add_cart
from cartdel import cartdel
from cus_hyouzi import hyouzi
from cus_henkou import henkou
from execute import sql_execute
stop = 0
while stop < 1:
    print('メニュー\n1:新規登録\n2:ショッピングカートにログイン\n3:お問い合わせ\n4:終了')
    menu = input('行いたい処理のメニュー番号を入力してください。（半角数字）>')
    if menu == '1':
        print('')
        sinkitouroku()
        print('')

    elif menu == '2':
        print('==========')
        x = login()
        stop1 = 0
        while stop1 < 1:
            print('')
            y = cartnull(x)
            print('ショッピングメニュー\n1:登録内容の表示・変更\n2:商品情報検索・一覧\n3:購入履歴表示\n4:お問い合わせ\n5:終了（ログアウト）')
            menu2 = input('行いたい操作のメニュー番号を入力してください。（半角数字）>')
            if menu2 == '1':
                print('==========')
                hyouzi()
                henkou()
                print('==========')
            elif menu2 == '2':
                print('==========')
                search_show()
                print('==========')
            elif menu2 == '3'

    elif menu == '3':
        print('')
        print('お問い合わせ\n')
        print('vv商店情報\n')
        print('メールアドレス:vv@vv.com\n')
        print('電話番号:012-3456-7890\n')
        print('')

    elif menu == '4':
        print('')
        print('終了します。')
        stop = stop + 1

    else:
        print('')
        print('入力内容が間違っています。もう一度入力してください。')
        print('')
