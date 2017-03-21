# Pythonでは全ての値がオブジェクト。
# 関数ですらオブジェクト
# オブジェクトであれば、変数に代入して利用できる
# 関数に別名をつけて利用したり、
# 関数の引数に関数を指定したり、
# 関数の戻り値に別の関数を指定できる！

# 関数を変数に代入
# def mul_func(a, b):
#     return  a * b
# def div_func(a, b):
#     return a / b
#
# func = mul_func # 丸括弧をつけず、関数名だけを指定すれば代入できる
# result = func(2,3)
# print(result)
#
# func2 = div_func
# result = func2(10,5)
# print(result)

#REPL
# def mul_func(a,b): return a*b
#
# mul_func(2,3)   # 関数名の直後に丸括弧と引数を指定した時
# mul_func        # 関数名だけを指定した時

# ここまでの話で学習者は、関数が変数に代入できることを確認し理解すれば良い。

# 関数の引数に関数を指定
# def mul_func(a,b): return a*b
# def add_func(a,b): return a+b
#
# def calc_5_3(func):
#     return func(5,3)
#
# result = calc_5_3(mul_func)
# print(result)
# result = calc_5_3(add_func)
# print(result)

# 関数定義しない関数：無名関数
# 名前のない関数をどう扱うの？ー＞変数に代入して扱う
# 定義の仕方
# v = lambda 引数,引数,引数... : 式
# ※lambda式の戻り値は「関数オブジェクト」となる。

#REPL
# x2 = lambda x : x * 2
# x2(2)
# x2(4)

# x2は変数であり、x * 2という関数オブジェクtが代入されたもの。
# 関数の定義と無名関数を使う違い
# def x2(x): return x * 2
# x2 = lambda x : x * 2

# 練習
# tri = lambda a,b : a * b / 2
# tri(13,15)

# 先ほどの、引数に関数を指定する関数の部分を、無名関数で書き換えよう
# def calc_5_3(func):
#     return func(5,3)
# # calc_5_3 = lambda func : func(5,3)
# print( calc_5_3(lambda a,b : a * b) )

# 後半


# リストに対する処理　map() filter()
# lambdaが役に立つのは、関数の引数に関数オブジェクトを指定したい場面

# lambdaをmap()とともに使う
# 構文：map(funtion, iterable)
# function:関数オブジェクト iterable:リストやタプルなどの複数の値を持てるデータ型
# map()は第一引数の関数を、第二引数のリストの要素すべてに適用し、結果を返す。
# REPL
# nums = [1,2,3,4,5]
# x2 = lambda x : x * 2
# list( map(x2, nums) )

# lambdaをfilter()と共に使う
# 構文：filter(function, iterable)
# 第一引数の関数を、第二引数のリスト要素すべてに適用し、結果がTrueな要素だけを返す。
# REPL
# nums = list(range(20))
# list(filter( lambda x : (x % 2) == 0, nums ))
# list(filter( lambda x : x > 13, nums ))

# リストや辞書型の値を並び替えよう
# リストを並び替え
# sorted()はすでに使ったことがあるが、lambdaを組み合わせると、より自由に並び替えができる。
# 構文：sorted(iterable [, key(function)][, reverse])
# key(function)には無名関数を指定する。reverseはデフォルトでFalseだが、Trueにすると大きい順（降順）になる。
# animal_list = [
#     ("Lion", 58),
#     ("Cheetah", 110),
#     ("Zebra", 60),
#     ("Reindeer", 80)
# ]
# faster_list_l = sorted(
#     animal_list,
#     key = lambda ani : ani[1],
#     #reverse = True
# )
# print("faster_list_l =", faster_list_l)
# for i in faster_list_l:
#     print(i)

# dict型をソートする
animal_dict = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80
}
faster_list_d = sorted(
    animal_dict.items(),
    key= lambda ani : ani[1],
    reverse= True
)
print(faster_list_d)
for i in faster_list_d:
    print(i)
for a, b in faster_list_d:
    print(a, b)

# まとめ
# 無名関数lambda
# lambdaはリストに関する処理に役立つ。map(),filter(),sorted()が主要な関数
