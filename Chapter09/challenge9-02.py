text = input("あなたの好きな食べ物は?:")
with open("food.txt", "w", encoding="utf-8") as f:
    f.write(text)


print("ファイルに書き込みました。")


