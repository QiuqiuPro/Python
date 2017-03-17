#関数の定義
# def 関数名(引数):
#     関数の処理
#     ・
#     ・
#     ・
#     return 戻り値

# 循環を、関数の入れ子で表現
# for i in range(10):
#     print("Hello",i)

# def say_hello(i):
#     if i <= 0:
#         return
#     print("hello",i)
#     say_hello(i-1)
# say_hello(10)

# 階乗 n!
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# 引数の名前を指定
# def calcTime(dist, speed):
#     return round(dist/speed, 1)
# print( calcTime(500,100) )
# print( calcTime(dist=500, speed=100) )

# 可変長引数. タプルとして代入されている。
# def sumArgs(*args):
#     print("args =",args)
#     v = 0
#     for n in args:
#         v = v + n
#     return v
# print( sumArgs(2,3,4,4,6,7,5,7,5) )

# 辞書型にもできる
# def print_args(**args):
#     print(args)
# print_args(a=30, b=49, c=99)
# print_args(bb="hoge", cc="fuga")

# ローカル変数とグローバル変数
# value = 100 #global
# def changeValue():
#     # 関数内で利用される変数のことを「ローカル変数」と呼んで、外と区別している。
#     #global value
#     value = 20 #local
#     return value
# print("local value =",changeValue())
# print("global value =",value)

# 例
# age = 0
# print("my age is {age}".format(age=23))
# print("age =",age)
