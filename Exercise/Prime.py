# 宿題：素数を返すイテレータを作ろう(30まで。)
# ヒント：素数とは、1と自分自身以外の整数で割り切れないような整数。30まで。
from time import time ########################3

from math import sqrt

start_t = time() ########################3

def dividable(lst, num):
    ''' return True if any number in [lst] can divide [num].
    Otherwise return False. '''
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

def funcListPrime(until_num):
    list_p = []
    for i in range(2, until_num+1):
        if dividable( list_p, i ) == False:
            list_p.append(i)
            print("*",end="")
        else:
            print(" ",end="")
            continue
    return list_p

# ite = genPrime(300000)
# # for i in ite:
# #     print(i)
# prime_l = list(ite)
# print(prime_l[-1])
# print(len(prime_l))

lstPrime = funcListPrime(300000)
# print(len(lstPrime))

end_t = time()
print("\n",end_t - start_t)
