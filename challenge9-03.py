import csv 

  

movies = [ 
    ["Top Gun", "Risky Business", "Minority Report"], 
    ["Titanic", "The Revenant", "Inception"], 
    ["Training Day", "Man on Fire", "Flight"]
  
] 

  

with open("moves.csv", "w", newline='')as f: 
    w = csv.writer(f) 
    w.writerows(movies) 

