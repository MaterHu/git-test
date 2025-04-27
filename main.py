print("这是一个打招呼程序。")
user = input('请输入姓名：')
# print(f"hello,{user}")

# 这是一个打招呼测试的业务
# def greeting(user):
#     print(f"hello,{user}")


def greetingBylevel(user):
    if user == 'MaterHu':
        print(f'hello,{user} sama!')
    else:
        print(f'hello,{user}!')


greetingBylevel(user)

