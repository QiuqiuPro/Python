# # iterator & generator
# # イテレータ(iteretor) <≈ iterable(リスト、タプルなど
# # 日本語で言うと「反復子」であり、値を一つずつ順に取り出すための仕組み。
# # REPL
# >>> list(map( lambda x : x * 2, [1,2] ))
# [2, 4]
# >>> list(map( lambda x : x * 2, range(2) ))
# [0, 2]
# # イテレータの代表的な利用例がfor構文。
# # ジェネレータ(generator)は独自のイテレータを作成する仕組み。
# # 具体的には、関数の中でyield文を使うと、関数の実行状態を保ったまま、途中で別の処理を実行することができる。

# # for構文を利用するときには、range()関数やリストを用いてきました。
# for i in range(1,4):
#     print(i)
# print("---")
# nums = [2,4,6]
# for i in nums:
#     print(i)
#
# # 書式（for構文の詳しい使い方）：
# for 対象 in 反復可能な値:
#     処理
#
# # 反復可能な値とは「イテレータを生成することができるオブジェクト」という意味。
# # 実際にfor構文の動作を手順で書き出すと、以下のようになる。
# # (1)反復可能な値からイテレータを生成する
# # (2)イテレータから値を一つ取り出す。値が取り出せたら手順(3)に移り、取り出せなければ、そこで繰り返しを終了する
# # (3)処理ブロックを実行する
# # (4)手順2に戻る

# #p.143
# # イテレータとは、値を一つずつ順に取り出すことのできる仕組みを持つオブジェクト。
# # そもそも、range()関数は、任意の個数の整数を取り出すことができるイテレータを生成する関数。
# # リストは任意の値を取り出すことができるイテレータを生成可能なデータ型。
# # REPL
# nums = [1,2,3]
# iter(nums)
# i = iter(nums)
# next(i)
# next(i)
# next(i)
# next(i)
# # つまり、for構文はイテレータから順に値を取り出していって、このエラーが出るまで繰り返し処理を行うという仕組み
# rangeでも同じ。
# # range()関数とイテレータ
# # REPL
# i = iter(range(1,4))
# i
# next(i)
# ...

# # ジェネレータ：自作のイテレータを作ろう
# # ジェネレータを使ってイテレータを作るには、関数を定義すれば良い。
# # ただし、普通の関数と違うのは、値を返すのにyield文を使うこと。<->（普通の関数はreturn）
# # yield文を使うと、"関数内の状態をすべて保存"します。そして、再度その関数が呼ばれると、
# # 先ほどyieldで値を返した直後から処理を継続実行する
# def gen1to3():
#     yield 1
#     yield 2
#     yield 3
#
# it = gen1to3() #イテレータオブジェクトをitに代入
# for i in it:
#     print(i)

# # forではなくnextを使って一歩一歩見てみよう
# # REPL
# def gen1to3(): yield 1; yield 2; yield 3
#
# i = gen1to3()
# i
# next(i)

# # 練習問題：奇数を返すイテレータを作ろう(30まで。)
# def genOdd():
#     i = 1
#     while i <= 30:
#         yield i
#         i += 2
#
# it = genOdd()
# for v in it:
#     print(v)

# 宿題：素数を返すイテレータを作ろう(30まで。)
# ヒント：素数とは、1と自分自身以外の整数で割り切れないような整数。30まで。
def dividable(lst, num):
    ''' return True if any number in [lst] can divide [num].
    Otherwise return False. '''
    # 一度でも割られてしまうと、アウト（素数ではない）。
    for i in lst:
        if i <= 1:
            continue
        elif num % i == 0:
            return True
        elif num % i != 0:
            continue
    else:
        return False

# generator that gives Prime numbers.
def genPrime(until_num):
    primes = []
    for i in range(2, until_num+1):
        try:
            # judge if is prime num
            if dividable( primes, i ) == False:
                primes.append(i)
                yield i
            else:
                continue
        except:
            break

ite = genPrime(30)
for i in ite:
    print(i)
