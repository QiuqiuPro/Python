# coding: utf-8

print("{0:=^41}".format("iterator_prime begin"))

n = int(input("Please input a number:\n"))
prime_list = [2]
for i in range(3,n,2):
    juage = False
    for j in iter(prime_list):
        if (j!=i) and (i%j == 0):
            juage = True
            break
        else:
            j += 2
    if juage == False:
        prime_list.append(i)
print("Prime numbers smaller than {0}:\n {1}".format(n,set(iter(prime_list))))

print("{0:=^41}".format("iterator_prime end"))
