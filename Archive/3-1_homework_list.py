book = []
students = ["Hanako","Yukio","Akio","Kiyoko","Ichiro"]

for i in range(0,len(students)):
    score = int(input("{0}'s score:".format(students[i])))
    book.append([students[i],score])
print(book)

book_NG = []
book_OK = []
while len(book) > 0:
    if book[0][1] > 60:
        book_OK.append(book[0])
    else:
        book_NG.append(book[0])
    del book[0]
print(book,book_NG,book_OK)
