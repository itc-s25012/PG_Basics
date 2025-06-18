import csv 

  

movies = [ 
    ["Top Gun", "Risky Business", "Minority Report"], 
    ["Titanic", "The Revenant", "Inception"], 
    ["Training Day", "Man on Fire", "Flight"]
  
] 

  

with open("moves.csv", "w", newline='', encoding="utf-8")as f: 
    w = csv.writer(f)
    for row in movies:
    w.writerows(row) 

