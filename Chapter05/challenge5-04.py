profile = {"名前": "與儀真妃",
           "身長":"156.7cm",
           "好きな色":"緑",
           "好きな漫画":"真夜中のオカルト公務員,憂国のモリアーティ",
           "得意分野":"水泳,ゆるいキャラクターを描くこと,創作ダンス"
           }

n = input("知りたい情報のキーを入力してください:")
if n in profile:
    introduction = profile[n]
    print(introduction)
else:
    print("見つかりません")

