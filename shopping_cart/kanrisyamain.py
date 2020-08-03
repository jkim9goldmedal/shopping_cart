def kanrisyazentai():
    stop = 0
    while stop < 1:
        print('メニュー\n1:日ごとの売上一覧出力\n2:月ごとの売上一覧出力\n3:終了')
        menu = input('行いたい処理のメニュー番号を入力してください。（半角数字）>')
        if menu == '1':
            import zyutyunull_uriage
            y = zyutyunull_uriage.zyutyu_null_day()
            if y == [0]:
                print('受注情報はありません。メインメニューに戻ります。')
            else:
                import day_uriage_txt
                day_uriage_txt.day_uriage_txt()
                print('====================')

        elif menu == '2':
            import zyutyunull_uriage_month
            y = zyutyunull_uriage_month.zyutyu_null_month()
            if y == [0]:
                print('受注情報はありません。メインメニューに戻ります。')
            else:
                import month_uriage_txt
                month_uriage_txt.month_uriage_txt()
                print('====================')

        elif menu == '3':
            print('終了します。')
            stop += 1
        else:
            print('正しい数を入力してください。')
kanrisyazentai()
