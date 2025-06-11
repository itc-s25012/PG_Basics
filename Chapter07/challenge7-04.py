correct_numbers = [3, 5, 9]

while True:
    user_input = input("数字を入力してね（qで終了）: ")
    if user_input == 'q':
        print("終了します")
        break
    elif user_input.isdigit():
        number = int(user_input)
        if number in correct_numbers:
            print("正解！")
        else:
            print("不正解")
    else:
        print("数字を入力するか、qで終了してね")

