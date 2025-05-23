def f(a):
    """
    文字列をfloatにして数字に変換
    引数aは文字列型
    返り値bはfloat型
    """
    try:
        b = float(a)
        return b
    except ValueError:
        return "数字を入れてください"



print(f("7"))
print(f("a"))
