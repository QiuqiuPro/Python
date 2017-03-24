# # ファイル処理とwith構文
# # 書式・手順：
# # (1)ファイルを開く
# open()
# # (2)ファイルを読み書きする
# read()
# write()
# # (3)ファイルを閉じる
# close()

# #1 open
# a_file = open("SampleText.txt", encoding="utf-8")
# #2 read
# s = a_file.read()
# #3 close
# a_file.close()
# #print out.
# print(s)

# #1 open
# a_file = open("SampleText.txt", mode="a", encoding="utf-8")
# #2 write
# a_file.write("I've never failed.\n")
# #3 close
# a_file.close()

# # open()のmode引数に与える値
# w #書き込みモードで
# r #読み込みモードで　（デフォルト）
# a #書き込み用に開き、ファイルが存在すれば末尾に追記する
# b #バイナリモード
# t #テキストモード　（デフォルト）

# # try... finallyで確実に閉じよう
# a_file = open("SampleText.txt", mode="w")
# try:
#     a_file.write("私は一度も失敗したことがない\n")
#     a_file.write("ただ、一万通りの方法を見つけただけだ")
# finally:
#     a_file.close()

# # with構文を使うと記述を簡潔にできる
# with open(ファイル名)　as 変数名:
#     読み書き処理

# with open("SampleText.txt", mode="a") as f:
#     f.write("私は失敗したことがない。\n")
#     f.write("ただ、一万通りの方法を見つけただけだ\n")

# # テキストファイルを1行ずつ処理しよう
# with open("SampleText.txt", encoding="utf-8") as tf:
#     for idx, line in enumerate(tf):
#         if idx < 5:
#             print(idx, line)


# # テキストからキーワードを探す
# key="find"
# with open("SampleText.txt", encoding="utf-8") as tf:
#     for idx, line in enumerate(tf):
#         if line.find(key) >= 0:
#             print(idx+1, ":", line)

# 1行ずつ読み込む利点
# 大きなファイルを処理するときに、全部をいっぺんに処理しようとするとメモリを占領してしまいエラーとなる。
# しかし1行ずつなら大きなファイルでも問題なく処理できる。

# # Pythonのオブジェクトや変数を保存しよう。
# # 複雑なデータ型を保存するのに便利なのがjson形式。
# # 書式（関数とその説明）：
# json.dumps(obj)     #オブジェクトをJSON文字列に変換
# json.loads(json)    #JSON文字列をPythonオブジェクトに変換
# json.dump(obj, fp)  #オブジェクトをJSON形式でファイルに保存
# json.load(fp)       #JSON形式のファイルからデータを読み出す
# # ＊fpで示した部分には、open()関数の戻り値を指定する

# # 実践
# import json
#
# data = {
#     "no": 5,
#     "code": ("jas", 1, 19),
#     "list": [1,2,3],
#     "scr": "be quick to listen, slow to speak, slow to anger",
# }
#
# filename = "SampleJson.json"
# with open(filename, "w") as fp:
#     json.dump(data, fp)
#
# with open(filename, "r") as fp:
#     r = json.load(fp)
#     print("no=", r["no"])
#     print("code=", r["code"])
#     print("list=", r["list"])
#     print("scr=", r["scr"])

import json
yobi = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
with open("yobi.json", "w") as f:
    json.dump(yobi, f)
