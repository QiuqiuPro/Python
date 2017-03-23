# # 複数のモジュールを組み合わせたものをパッケージと呼ぶ。
# # 様々なPythonのパッケージが有志により公開されており、そうしたパッケージが多数登録されているのがPyPIです。
# # https://pypi.python.org/pypi
# # パッケージ管理ツールpip
# # 書式：
# $ pip install パッケージ名
#
# $ pip install pillow qrcode
# # if you are asked to update pip, -U option to update.
# $ pip install -U pip

# import qrcode # import package
# img = qrcode.make("https://github.com/QiuqiuPro/Python") #generate QRcode
# img.save("qrcode_github-qiuqiupro.png") #save in file.

# $ pip uninstall SomePackage #how to uninstall.

# $ pip install pycrypto
# # WindowsではMicrosoftvirtualstudioが必要。時間がかかるので、minicondaをインストールすると、PyCryptoが利用できる。（上のコマンドは不要）
# # *p.168


# 暗号化・復号化するプログラムを描いてみよう
from Crypto.Cipher import AES #(1)
import base64

# 暗号化したいデータとパスワードを指定(2)
message = "自分がしてほしいと思うことを人にもするように"
password = "WE23RHgSGb24" # 適当なパスワードを指定
iv = "Lpo23G4ub5Tqe4YU" # 初期化ベクトル（16文字で適当な値を指定）
mode = AES.MODE_CBC # 暗号化モードを指定

# 特定の長さの倍数にするため空白でデータを埋める関数(3)
def mkpad(s, size):
    s = s.encode("utf-8")
    pad = b' ' * (size - len(s) % size) # 特定の長さの倍数にするための空白を生成
    print("mkpad", s + pad)
    return s + pad

# 暗号化する(4)
def encrypt(password, data):
    # 特定の長さに調節する
    password = mkpad(password, 16)
    data = mkpad(data, 16)
    password = password[:16]
    # 暗号化
    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data) # バイト列
    # base64~=文字列が内容のバイト列形式 | decode("utf-8")＝文字列
    return base64.b64encode(data_cipher).decode("utf-8")

# 復号化する(5)
def decrypt(password, encdata):
    # パスワードの文字数を調節
    password = mkpad(password, 16)
    password = password[:16]
    # 復号化
    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)
    data = aes.decrypt(encdata)
    return data.decode("utf-8")

# 暗号化する
enc = encrypt(password, message)
# 復号化する
dec = decrypt(password, enc)

# 結果を表示する
print("暗号化：", enc )
print("復号化：", dec )
