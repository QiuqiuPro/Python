list1 = ['a', 'b', 'c']
list2 = [1,2,3]
zip(list1, list2) #=> zip object
list(zip(list1,list2)) #=> [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs) #=> ('a', 'b', 'c'), (1, 2, 3)
# *を引数につけると引数展開が行われる。
# そのためletters, numbers = zip(('a', 1), ('b', 2), ('c', 3))
# と同じことになる

# 引数展開は普遍的に使える
# REPL
def add(a,b): return a+b

add(1,2)    #=>3
add([1,2])  #=>TypeError
add(*[1,2]) #=>3
