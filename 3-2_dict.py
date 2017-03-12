リストと同じように、複数の値を一つの変数で管理することができるのだが、
リストがインデックスで値を参照するのに対して、
辞書型は任意のキー文字列で値を参照する。
d = { 'Height':180, 'Weight':51 }
d['Height']
d['Weight'] = 55    #書き換え
d['Age'] = 23       #追加

food_price = { "Apple":100, "Banana":180, "Tomato":400 }
"Tomato" in food_price
"Orange" in food_price
food_price["Tomato"]

food_price.keys()
#=> dict_keys(['Apple', 'Orange'])
リストではなく、dict_keys型であると言うこと。
list( food_price.keys() )
sorted( food_price.keys() ) #文字コード順

list( d.values() )
list( d.items() )

p.105
food_price = { "Apple":100, "Banana":180, "Tomato":400 }
for name in food_price.keys():
    price = food_price[name]
    print("{0} is {1} yen.".format(name,price))

for name, price in food_price.items():
    print("{0} is {1} yen.".format(name,price))

#複数の値を複数の変数に割り当てる
name, price = ["Mikan", 100]
a, b, c = [2, 45, 216]


# PRACTICE!!!
records = {
    'Tanaka':72, 'Yamada':65, 'Hirata':100,
    'Akari':56, 'Fukuda':66, 'Sakai':80}
# see sum
sum_v = 0
for v in records.values():
    sum_v += v
# see ave
ave_v = sum_v / len(records)
print("Sum points:", sum_v)
print("Ave points:", ave_v)

# print a table
fmt = "|{0:<7}|{1:>4}|{2:>5}|"
print(fmt.format("Name","Score","Diff"))
for name, v in sorted( records.items() ):
    diff_v = v - ave_v
    diff_v = round(diff_v, 1)
    print(fmt.format(name, v, diff_v))


# PRACTICE 2
poem =
'''
Three sang of love together: one with lips
Crimson, with cheeks and bosom in a glow,

Flushed to the yellow hair and finger tips;
And one there sang who soft and smooth as snow
Bloomed like a tinted hyacinth at a show;

And one was blue with famine after love,
Who like a harpstring snapped rang harsh and low

The burden of what those were singing of.

One shamed herself in love; one temperately
Grew gross in soulless love, a sluggish wife;

One famished died for love. Thus two of three
Took death for love and won him after strife;

One droned in sweetness like a fattened bee:
All on the threshold, yet all short of life.
'''
poem = poem.replace(":","")
poem = poem.replace(";","")
poem = poem.replace(",","")
poem = poem.replace(".","")
words = poem.split() #"an apple".split()

counter = {}
for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

for k, v in sorted( counter.items() ):
    if v >= 3:
        print(k,v)
