# # リスト内包表記
# # List Comprehensionsとは、複雑な値を持つリストヤタプル・辞書型を手軽に生成するための表記方法。
# # 比較
# # for文を使った繰り返しで作る
# data = []
# for i in range(1,6):
#     data.append(i * 2)
# print(data)
# # 無名関数とmap()を使って作る
# data2 = list( map( lambda x: x*2, range(1,6) ) )
# print(data2)
# # リスト内包表記を使って作る
# data3 = [ i*2 for i in range(1,6) ]
# print(data3)
# # 速度的にリスト内包表記の方が早く、シンプル。

# # 練習：10以下の奇数を持つリストを作る。
# # 練習が終わったら、以下に進む
# odd_under_ten1 = [ 2*n - 1 for n in range(1,6) ]
# odd_under_ten2 = [ i for i in range(1,11,2) ]
# odd_under_ten3 = [ i for i in range(1,11) if i%2 == 1 ]
# print(odd_under_ten1,odd_under_ten2,odd_under_ten3, sep="\n")

# リスト内包表記のif
# リスト内包表記ではforのあとにifを記述して内容をフィルタリングできる
# 書式：
# [ 式 for .. in .. if .. ]

# ネストした内包表記
# for構文を多重にネストして使うことができる。
# result = []
# base = [1,2,3]
# for x in base:
#     for y in base:
#         result.append( (x,y) )
# print(result)
#
# base = [1,2,3]
# result = [ (x,y) for x in base for y in base ]
# print(result)
#
# base = [1,2,3]
# result = [ (x,y) for x in base for y in base if x != y ]
# print(result)

# # 三項演算子
# # 書式
# # 変数 = Trueの値 if 条件 else Falseの値
# # REPL
# n = 3
# print("偶数" if (n%2==0) else "奇数")

# 内包表記の種類
# リスト内包表記
# 集合型内包表記
# 辞書内包表記
# ジェネレータ式
# REPL
[ x**2 for x in [1,2,3]]
{ (x+y) for x in [1,2,3] for y in [1,2,3]}
{ "Dice"+str(x) : x for x in range(1,7)}
# ジェネレータ式
( x**2 for x in [1,2,3])
gen = ( x**2 for x in [1,2,3])
next(gen)
