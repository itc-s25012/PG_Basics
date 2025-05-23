def add_it(a, b, c, d=10 , e=12):
    """
    3つの必須引数と2つのオプション引数を足し算する
    必須引数はa, b, c  オプション引数は、d,e
    返り値　a + b + c + d + e は整数型
   """ 
    return a + b + c + d + e


result = add_it(1,2,3)
print(result)




result = add_it(1,2,3,4,5)
print(result)

