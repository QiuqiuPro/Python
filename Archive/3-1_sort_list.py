list_a = [6,3,8,4,1,2,9,5,7]
print("start\n",list_a, end="\n\n\n")
'''
for j in range(len(list_a)-1,0,-1):
    #swapped_at_least_once = False
    for i in range(0,j):
        if list_a[i] > list_a[i+1]:
            list_a[i:i+2] = [ list_a[i+1], list_a[i] ]
            print(list_a)
    #        swapped_at_least_once = True
        else: print("[{0:^25}]".format("no swap"))
    print("\n{0:^25}\n".format("*"))
    #if swapped_at_least_once == False:
    #    break
print("\nfinal\n", list_a)
'''
#"""
for j in range( len(list_a)-1, 0, -1 ):
    for i in range(0,j):
        if list_a[i] > list_a[i+1]:
            list_a[i:i+2] = [ list_a[i+1], list_a[i] ]
print(list_a)
#"""
