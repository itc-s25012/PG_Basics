import csv
movies_japanese = [
    ["トップガン", "リスキー・ビジネス", "マイノリティ・リポート"],
    ["タイタニック", "レヴェナント", "インセプション"],
    ["トレーニング・デイ", "マン・オン・ファイア", "フライト"]

]


with open("movies_ja.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f)
    for row in movies_japanese:
    w.writerows(row)

