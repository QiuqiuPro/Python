#REPL
""
''
""""""
''''''
str(12)
s1 = "abc"
s2 = "def"
s = s1 + s2
s = "@"
s * 3
"love" * 3
s = "abcde"
s[0]
s[1:4]
s = "0123456789"
s[5:8]
s[3:]
s[:5]
s[-1]
s[-3:]
s[0:9:2]
s[::3]

s = "This is a pen"
s.split()
s = "2017/03/13"
s.split("/")
s.split("/",maxsplit=1)
a = ["aaa","bbb","ccc"]
"-".join(a) #list, tuple, set...
# * join is a method of str class.

#py
date = "2017/03/13"
date_list = date.split("/")
new_date = "-".join(date_list)
print(new_date)

date.replace("/","-")
#str.replace(old,new[,count])

#other methods is placed p.115. see when you need.
