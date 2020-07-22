def kanrisyazentai():
    stop = 0
    while stop < 1:
        print('メニュー\n1:日ごとの売上一覧出力\n2:月ごとの売上一覧出力\n3:終了')
        menu = input('行いたい処理のメニュー番号を入力してください。（半角数字）>')
        if menu == '1':
            import zyutyunull_uriage
            y = zyutyunull_uriage.zyutyu_null()
            if y == ():
                print('受注情報はありません。')
            else:
                import day_uriage_txt
                day_uriage_txt.day_uriage_txt()
                print('====================')
                print('出力が完了しました。')
        elif menu == '2':
            import zyutyunull_uriage
            y = zyutyunull_uriage.zyutyu_null()
            if y == ():
                print('受注情報はありません。')
            else:
                import month_uriage_txt
                month_uriage_txt.month_uriage_txt()
                print('====================')
                print('出力が完了しました。')
        elif menu == '3':
            stop += 1
        else:
            print('正しい数を入力してください。')
kanrisyazentai()
