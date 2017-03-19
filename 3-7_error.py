# エラーが起きるとプログラムが終了してしまう。
# REPL
# 3 / 0

# エラーに対処するための構文
# 構文：
# try:
#     何らかの処理
# except:
#     エラーが起きた時の処理

# りんごを分けるプログラム
# 入力を求める
# n個のりんごをx人で割る。
# もし0人の場合、入力ミスを忠告する
# ppl = int(input("How many people?\n"))
# apples = 10
# try:
#     print( "each person can eat {0} apple(s).".format( round( apples/ppl, 1 ) ) )
# except:
#     print("入力ミスがあります。0より大きい数字が入力されていることを確認してください")

# 特定のエラーだけ補足する
# 構文：
# try:
#     何らかの処理
# except エラーの種類1:
#     エラーの種類1に応じた処理
# except (エラーの種類2, エラーの種類3, ...):
#     複数のエラーの種類に応じた処理
# except エラーの種類5 as e:
#     エラー種類5に応じた処理
#     eにエラーの詳細情報が得られる
# except:
#     上記以外のエラーに応じた処理

# apples = 10
# try:
#     ppl = int( input("How many people?\n") )
#     print( "each person can eat {0} apple(s).".format( round( apples/ppl, 1 ) ) )
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("other error")

# エラーの有無に関わらず最後まで実行したい時
# ファイルなどのリソースを扱う際には必ず最後にリソースを閉じる終了処理を行わなければならない。
# 書式：
# try:
#     リソースを扱う処理
# except:
#     エラー処理
# finally:
#     リソースを閉じるなど必ず実行する処理

# エラーを発生させる。
# わざとエラーを発生させることができます。
# 書式：
# raise エラー種類(メッセージ) # エラー種類は定義済みのものであることが必要。
# REPL
# raise Exception("Hello, Error")

# for構文と同じ機能の関数を作ってみよう。
# イテレーターの章が既習であることが必要。
