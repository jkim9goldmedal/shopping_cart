def shopping_cart():
    import pymysql
    stop = 0
    while stop < 1:
        print('メニュー\n1:新規登録\n2:ショッピングカートにログイン\n3:お問い合わせ\n4:終了')
        menu = input('行いたい処理のメニュー番号を入力してください。（半角数字）>')
        if menu == '1':#新規登録：済み
            print('===========')
            import tourokunew
            tourokunew.tourokunew()
            print('===========')

        elif menu == '2':#ログイン
            print('==========')

            import login
            x = login.login()
            stop1 = 0
            while stop1 < 1:
                print('==========')
                import cartnull
                y = cartnull.cartnull(x)
                print('ショッピングメニュー\n1:登録内容の表示・変更\n2:商品情報検索・一覧\n3:購入予定明細表示\n4:購入履歴表示\n5:お問い合わせ\n6:終了（ログアウト）')
                menu2 = input('行いたい操作のメニュー番号を入力してください。（半角数字）>')
                if menu2 == '1':#登録内容変更：済み
                    print('==========')
                    import cus_hyouzi
                    cus_hyouzi.hyouzi(x)
                    print('==========')
                    henkaku = input('変更しますか？(1:はい 2:いいえ)>')
                    if henkaku == '1':#変更する
                        import cus_henkou
                        cus_henkou.henkou(x)
                        stop1 += 1
                        print('==========')
                    elif henkaku == '2':#最初の画面に戻る
                        continue
                    else:
                        print('正しい数を入力してください。')
                elif menu2 == '2':#商品検索:済み
                    stop2 = 0
                    while stop2 < 1:
                        print('==========')
                        import search_show
                        search_show.search_show()
                        print('==========')
                        sentaku = input('行いたい処理を選択してください。\n1:カート追加・変更に進む\n2:メインメニューに戻ってショッピングを続ける\n3:終了する・ログアウト\n>')
                        if sentaku == '1':#カート追加
                            stop3 = 0
                            while stop3 < 1:
                                print('==========')
                                import cartnull_addcart
                                cartnull_addcart.cartnull_add(x)
                                import add_cart
                                add_cart.add_cart(x)
                                print('==========')
                                sentaku2 = input('行いたい処理を選択してください。\n1:カートの中身を表示する\n2:このままカートの追加・変更を行う\n3:商品検索に戻る\n4:メインメニューに戻ってショッピングを続ける\n5:終了する・ログアウト\n>')
                                if sentaku2 == '1':#購入予定明細：済み
                                    stop4 = 0
                                    while stop4 < 1:
                                        import cartnull
                                        y = cartnull.cartnull(x)
                                        if y == ():#カート内確認→商品ないとき：済み
                                            print('==========')
                                            print('カート内に商品がありません。カートに追加してから実行してください。')
                                            stop4 += 1
                                            stop3 += 1
                                            stop2 += 1
                                        else:#商品あるとき：済み
                                            print('==========')
                                            import cart_meisai
                                            cart_meisai.cart_meisai(x)
                                            print('==========')
                                            sentaku3 = input('行いたい処理を選択してください。\n1:購入する\n2:カート内の数量を変更する\n3:メインメニューに戻ってショッピングを続ける\n4:終了・ログアウト\n>')
                                            if sentaku3 == '1':#購入する:済み
                                                import zaikocheck
                                                check = zaikocheck.zaikocheck(x)

                                                if check == 1:
                                                    print('メインメニューに戻ります。')
                                                    stop4 += 1
                                                    stop3 += 1
                                                    stop2 += 1

                                                elif check == 0:
                                                    print('==========')
                                                    import meisai_text
                                                    meisai_text.meisai_text(x)
                                                    import cart_syori
                                                    cart_syori.cart_syori(x)
                                                    print('==========')
                                                    print('メインメニューに戻ります。')
                                                    stop4 += 1
                                                    stop3 += 1
                                                    stop2 += 1
                                                # elif lastkaku == '2':
                                                #     print('メインメニューに戻ります。カートの中身を確認後、もう一度購入してください。')
                                                #     stop4 += 1
                                                #     stop3 += 1
                                                #     stop2 += 1
                                                # else:
                                                #     print('正しい数を入力してください。')
                                            elif sentaku3 == '2':
                                                stop4 += 1

                                            elif sentaku3 == '3':#メインメニュー：済み
                                                stop4 += 1
                                                stop3 += 1
                                                stop2 += 1
                                            elif sentaku3 == '4':#終了（ログアウト）:済み
                                                import cartnull
                                                y = cartnull.cartnull(x)
                                                if y == ():
                                                    print('終了します。（カートに商品なし。）')
                                                    print('==========')
                                                    stop4 += 1
                                                    stop3 += 1
                                                    stop2 += 1
                                                    stop1 += 1
                                                    break
                                                else:
                                                    print('終了します。（カート内の商品は残っています。）')
                                                    print('==========')


                                                    stop4 += 1
                                                    stop3 += 1
                                                    stop2 += 1
                                                    stop1 += 1
                                                    break
                                            else:#入力エラー：済み
                                                print('==========')
                                                print('入力内容が間違っています。もう一度入力してください。')
                                                print('==========')


                                elif sentaku2 == '2':#カート追加ふたたび：済み
                                    print('もう一度追加してください。')
                                elif sentaku2 == '3':#商品検索：済み
                                    stop3 += 1
                                elif sentaku2 == '4':#ショッピングメインメニュー：済み
                                    stop3 += 1
                                    stop2 += 1
                                elif sentaku2 == '5':#終了：済み
                                    import cartnull
                                    y = cartnull.cartnull(x)
                                    if y == ():
                                        print('終了します。（カートに商品なし。）')
                                        print('==========')
                                        stop3 += 1
                                        stop2 += 1
                                        stop1 += 1
                                        break
                                    else:
                                        print('終了します。（カート内の商品は残っています。）')
                                        print('==========')


                                        stop3 += 1
                                        stop2 += 1
                                        stop1 += 1
                                        break
                                else:#入力エラー：済み
                                    print('==========')
                                    print('入力内容が間違っています。もう一度入力してください。')
                                    print('==========')


                        elif sentaku == '2':#ショッピングメインメニュー：済み
                            stop2 += 1
                        elif sentaku == '3':#終了：済み
                            import cartnull
                            y = cartnull.cartnull(x)
                            if y == ():#カートなし
                                print('終了します。（カートに商品なし。）')
                                stop1 += 1
                                break

                            else:#カートあり
                                print('終了します。（カート内の商品は残っています。）')

                                stop1 +=1
                                break

                        else:#入力エラー：済み
                            print('==========')
                            print('入力内容が間違っています。もう一度入力してください。')
                            print('==========')
                elif menu2 == '3':#購入予定明細:済み
                    stop5 = 0
                    while stop5 < 1:
                        import cartnull
                        y = cartnull.cartnull(x)
                        if y == ():#カート内確認→商品ないとき：済み
                            print('==========')
                            print('カート内に商品がありません。カートに追加してから実行してください。')
                            stop5 += 1
                        else:#商品あるとき：済み

                            print('==========')
                            import cart_meisai
                            cart_meisai.cart_meisai(x)
                            print('==========')
                            sentaku3 = input('行いたい処理を選択してください。\n1:購入する\n2:カート内の数量を変更する\n3:メインメニューに戻ってショッピングを続ける\n4:終了・ログアウト\n>')
                            if sentaku3 == '1':#購入する:済み
                                import zaikocheck
                                check = zaikocheck.zaikocheck(x)

                                if check == 1:
                                    print('メインメニューに戻ります。')
                                    stop5 += 1

                                elif check == 0:
                                    print('==========')
                                    import meisai_text
                                    meisai_text.meisai_text(x)
                                    import cart_syori
                                    cart_syori.cart_syori(x)
                                    print('購入が完了しました。')
                                    print('==========')
                                    print('メインメニューに戻ります。')
                                    stop5 += 1

                            elif sentaku3 == '2':
                                stopstop = 0
                                while stopstop < 1:
                                    print('==========')
                                    import cartnull_addcart
                                    cartnull_addcart.cartnull_add(x)
                                    import add_cart
                                    add_cart.add_cart(x)
                                    print('==========')
                                    sentaku2 = input('行いたい処理を選択してください。\n1:カートの中身を表示する\n2:もう一度商品を追加する\n3:メインメニューに戻ってショッピングを続ける\n4:終了する（ログアウト）\n>')
                                    if sentaku2 == '1':
                                        stopstop += 1
                                    elif sentaku2 == '2':
                                        print('もう一度商品を追加してください。')
                                    elif sentaku2 == '3':
                                        stopstop += 1
                                        stop5 += 1
                                    elif sentaku2 == '4':
                                        import cartnull
                                        y = cartnull.cartnull(x)
                                        if y == ():
                                            print('終了します。（カートに商品なし。）')
                                            print('==========')
                                            stopstop += 1
                                            stop5 += 1

                                            stop1 += 1
                                            break
                                        else:
                                            print('終了します。（カート内の商品は残っています。）')
                                            print('==========')
                                            stopstop += 1

                                            stop5 += 1

                                            stop1 += 1
                                            break

                            elif sentaku3 == '3':#メインメニュー：済み
                                stop5 += 1

                            elif sentaku3 == '4':#終了（ログアウト）:済み
                                import cartnull
                                y = cartnull.cartnull(x)
                                if y == ():
                                    print('終了します。（カートに商品なし。）')
                                    print('==========')
                                    stop5 += 1
                                    stop1 += 1
                                    break
                                else:
                                    print('終了します。（カート内の商品は残っています。）')
                                    print('==========')
                                    stop5 += 1
                                    stop1 += 1
                                    break
                            else:#入力エラー：済み
                                print('==========')
                                print('入力内容が間違っています。もう一度入力してください。')
                                print('==========')
                elif menu2 == '4':#購入履歴表示：済み
                    import zyutyu_null
                    y = zyutyu_null.zyutyu_null(x)
                    if y == [0]:
                        print('==========')
                        print('購入履歴がありません。メインメニューに戻ります。')
                    else:
                        import rireki
                        rireki.rireki(x)
                        print('==========')
                elif menu2 == '5':#お問い合わせ:済み
                    print('==========')
                    print('お問い合わせ\n')
                    print('vv商店情報\n')
                    print('メールアドレス:vv@vv.com\n')
                    print('電話番号:012-3456-7890\n')
                    print('==========')
                elif menu2 == '6':#終了：済み
                    import cartnull
                    y = cartnull.cartnull(x)
                    if y == ():
                        print('終了します。（カート内に商品なし。）')
                        stop1 += 1
                        print('==========')
                        break
                    else:
                        print('終了します。（カート内の商品は残っています。）')
                        print('==========')

                        stop1 += 1
                        break
                else:#入力エラー：済み
                    print('==========')
                    print('入力内容が間違っています。もう一度入力してください。')
                    print('==========')

        elif menu == '3':#お問い合わせ：済み
            print('==========')
            print('お問い合わせ\n')
            print('vv商店情報\n')
            print('メールアドレス:vv@vv.com\n')
            print('電話番号:012-3456-7890\n')
            print('==========')

        elif menu == '4':#終了：済み
            print('==========')
            print('終了します。')
            stop = stop + 1

        else:#入力エラー：済み
            print('==========')
            print('入力内容が間違っています。もう一度入力してください。')
            print('==========')
shopping_cart()
