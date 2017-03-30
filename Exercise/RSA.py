# p = 2 * p1 + 1
# q = 2 * q1 + 1
# N = p * q
# phi(N) = (p - 1) * (q - 1)
# e * d ≡ 1 mod phi(N)
# PK: e, N
# SK: d, p, q
#
# Enc: c ≡ m ** e mod N
# Dec: m ≡ c ** d mod N
#
# 大きさ
# N nearly equal 2**20
# p, q nearly equal 2**10
#
# eとphi(N)は互いに素

from math import sqrt
from random import randint
e = 2**16+1

# ある数がリストの中の数で割り切れるかどうかを真偽値で返す
# 引数：判断材料のリスト、判断対象の数
# 戻り値：真偽値（割り切れるとTrue,割り切れないとFalse）
def dividable(lst, num):
    ''' 例：if dividable( list_p, i ) == False: '''
    # 一度でも割られてしまうと、アウト（素数ではない）。
    for i in lst:
        if i <= 1:
            continue
        elif i > sqrt(num):
            return False
        elif num % i == 0:
            return True
        elif num % i != 0:
            continue
    else:
        return False

# 素数のリストを作成する
# 引数：いくつまでの数の中での素数を入れるのか
# 戻り値：素数のリスト
def listUpPrime(until_num):
    ''' 例：lstPrime = funcListPrime(300) '''
    list_p = []
    for i in range(2, until_num+1):
        if dividable( list_p, i ) == False:
            list_p.append(i)
        else:
            continue
    return list_p

# 要求された範囲内で条件を満たす素数をだす
# 引数：安全度要求値＝n（例：2^10 の 10）
# 戻り値：2^n ~ 2^(n+1)の範囲内の、p=2p1+1を満たす素数のリスト
def listUpSKpq(security_strength):
    ''' listUpSKpq(10) '''
    ss = security_strength
    from_num = 2**ss
    until_num = 2**(ss+1)
    list_cld_prime = listUpPrime( from_num )
    list_prt_prime = []
    for p in list_cld_prime:
        if 2*p+1 < from_num: continue
        if dividable( list_cld_prime, 2*p+1 ) == False:
            list_prt_prime.append( 2*p+1 )
        else:
            continue
    # print("len(list_prt_prime):",len(list_prt_prime))
    return list_prt_prime

# 条件を満たす素数のリストから、ランダムにpとqを選出する
# 引数：素数のリスト
# 戻り値：pとqのタプル
def getPQ(list_p):
    ''' getPQ(listUpSKpq(10)) '''
    global e
    while True:
        idx = randint(0,len(list_p)-1)
        p = list_p[idx]
        del list_p[idx]
        if (2*p+1)%e != 1: break
    while True:
        idx = randint(0,len(list_p)-1)
        q = list_p[idx]
        del list_p[idx]
        if (2*q+1)%e != 1: break
    return (p, q)

# 最大公約数
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

# 互いに素
def coprime(a,b):
    return gcd(a,b) == 1

# 秘密鍵公開鍵を作成
def getSKPK(tpl_pq):
    p = tpl_pq[0]
    q = tpl_pq[1]
    N = p * q
    phiN = (p-1) * (q-1)
    print("phiN:",phiN)
    global e
    # e = e%phiN
    print("coprime." if coprime(e,phiN) else "not coprime.")
    for i in range(e,phiN,2):
        print(".",end="")
        if (e*i)%phiN == 1:
            d = i
            break
    print("e,d:",e,d)
    if d == int(d): d = int(d)
    PK = { "N":N, "e":e }
    SK = { "d":d, "phiN":phiN }
    return PK, SK

# Enc: c ≡ m ** e mod N
def enc(PK, msg):
    e = PK["e"]
    N = PK["N"]
    c = (msg**e) % N
    return c

# Dec: m ≡ c ** d mod N
def dec(SK, PK, c):
    d = SK["d"]
    N = PK["N"]
    m = (c**d) % N
    return m

PK, SK = getSKPK(getPQ(listUpSKpq(10)))
print(PK, SK)
print('e*d%phiN=',(PK["e"]*SK["d"])%SK["phiN"])
c = enc(PK, 12345)
print("c:", c)
m = dec(SK, PK, c)
print("m:", m)
