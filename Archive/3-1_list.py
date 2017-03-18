#前半
#REPL

# list_a = [1,2,3,4,5]
# list_a
# list_a[0]
# list_a[3]
# list_a[0] = 6
# list_a
# len(list_a)
# type([])        #=>list
# type(range(5))  #=>range
# #rangeのスキップを詳しく。あとで相似のものが出てくる。


#python3

# until_ten = [1,2,3,4,5,6,7,8,9,10]
#
# sum_v = 0 #初期化。whileのi=0と同じ
# for i in until_ten:
#     sum_v += i #sum_v = sum_v + i と同じ。
#     print("add {0}, total is {1}".format(i, sum_v))
#
# ave_v = sum_v / len(until_ten)
# print("average is", ave_v)

#i = i + 1
#i += 1
#REPL
# list_ten = [1,2,3,4,5,6,7,8,9,10]
# print("sum is {0}, ave is {1}".format(sum(list_ten),sum(list_ten)/len(list_ten)))



# # until_ten = [1,2,3,4,5,6,7,8,9,10]
# # sum(until_ten)
# number_string = ["one", "two", "three"]


#p.92
# print("{0:-^51}".format("p92"))
# import random
# trump = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K","Joker"]
# card_index = random.randint(0,len(trump)-1)
# print(trump[card_index])
#
# #list(enumerate())
# print("{0:-^51}".format("p93"))
# for index, value in enumerate(trump):
#     print(index,value)
#
# print( list(enumerate(trump)) )


# #リストを操作する
# list_a.append()
# [1,2]+[3,4]
# list_a+=[3,4]
# list_a.extend([3,4])
# list_one_to_ten=list(range(1,11))
# #スライス
# list_one_to_ten[1]
# list_one_to_ten[1:3]
# list_zero_to_nine=list(range(10))
# list_zero_to_nine[1:3]
# list_zero_to_nine[:3]
# list_zero_to_nine[5:]
# list_zero_to_nine[-1]
# list_zero_to_nine[-3:]
# list_zero_to_nine[2:8:2] #インデックス2から8未満まで、+2ずつでインデックスを見ていく
# list_zero_to_nine[::3]
# #要素の削除
# del list_zero_to_nine[5]
# del list_zero_to_nine[3:7]
# #その他のものは、参照場所p97とだけ知っていれば良い。


#見せる

#リストlistの仲間
#タプルtuple
#集合型set
# tuple_a = (1,2,3)
# tuple_a[1]=4 #=>Error
# list(tuple_a)
# tuple(list_a)
# set_a={1,2,2,3}
# set_b={2,4,5}
# set_a - set_b
# 2 in set_a
# set_a | set_b #+ではない
# set_a & set_b
# set(list_a)
