# coding: utf-8
# 九九
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}x{1}={2:>2}".format(j,i,i*j) , end=" ")
    print("")
