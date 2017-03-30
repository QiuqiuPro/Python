# # p.233
# #REPL
# from sklearn import datasets
# digits = datasets.load_digits()
# digits.images.shape
#
# digits.target[0]
# digits.images[0]

# # 上のデータを描画してみる
# from sklearn import datasets
# from matplotlib import pyplot as plt, cm
#
# digits = datasets.load_digits()
# i = 120
# data = digits.images[i]
#
# plt.imshow(data.reshape(8, 8), cmap=cm.gray_r, interpolation='nearest')
# plt.show()


# ##from sklearn import datasets, cross_validation, svm, metrics
# ## cross_validation will be removed and moved into model_selection in v0.20.
# from sklearn import datasets, model_selection, svm, metrics
#
# # 手書き数字データを読み込む
# digits = datasets.load_digits()
# # 訓練用データとテスト用データに分ける
# data_train, data_test, label_train, label_test = \
#     model_selection.train_test_split(digits.data, digits.target)
#
# # SVMアルゴリズムを利用してモデルを構築する
# # SVMアルゴリズムのSVCクラスを用いて分類。SVC,LinearSVC,NuSVCなどがある。
# clf = svm.SVC(gamma=0.001)
# #clf = svm.LinearSVC()
# # fit()を使うと学習することができる。引数1：訓練データ本体、引数2：訓練データに対するラベル
# clf.fit(data_train, label_train)
#
# # テストデータでの分類結果予測してみる
# # predict()メソッドを使うと、学習済みデータを元に、テストデータの分類を予測することができる。
# predict = clf.predict(data_test)
#
# # 結果を表示する
# ac_score = metrics.accuracy_score(label_test, predict) # 正解率を出すメソッドaccuracy_score()
# cl_report = metrics.classification_report(label_test, predict) # レポートを出すメソッドclassification_report()
# print("分類機の情報＝", clf)
# print("正解率＝", ac_score)
# print("レポート＝\n", cl_report)
# # precision:精度 recall:再現率（正解した割合） fl-score:精度と再現率の調和平均 support:正解ラベルのデータ数
# # precision(適合率):TP/(TP+FP) recall(再現率):TP/(TP+FN)


# 学習させたデータをファイルに保存しておいて、それを用いて新たな画像を認識させてみよう。
import os, sys, math
from sklearn import datasets, svm
from sklearn.externals import joblib

# モデルデータファイル名
DIGITS_PKL = "digit-clf.pkl"

# 予測モデルを作成する
def train_digits():
    # 手書きのデータを読み込む
    digits = datasets.load_digits()
    # 訓練する
    data_train = digits.data
    label_train = digits.target
    clf = svm.SVC(gamma=0.001)
    clf.fit(data_train, label_train)
    # 予測モデルを保存
    joblib.dump(clf, DIGITS_PKL) # json.dump(data, filename)
    print("予測モデルを保存しました=", DIGITS_PKL)
    return clf

# データから数字を予測する
def predict_digits(data):
    # モデルファイルを読み込む
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits()
    clf = joblib.load(DIGITS_PKL)
    # 予測
    n = clf.predict([data])
    print("判定結果=", n)

# 手書き数字画像を8x8のグレースケールのデータ配列に変換
def image_to_data(imagefile):
    import numpy as np
    from PIL import Image
    image = Image.open(imagefile).convert('L')
    image = image.resize((8,8), Image.ANTIALIAS)
    img = np.asarray(image, dtype=float)
    img = np.floor(16 - 16 * (img / 256)) # 行列演算
    # 変換後の画像を表示（下4行コメントインするとみれる）
    # import matplotlib.pyplot as plt
    # plt.imshow(img)
    # plt.gray()
    # plt.show()
    img = img.flatten()
    print(img)
    return img

def main():
    # コマンドライン引数を得る
    if len(sys.argv) <= 1:
        print("USAGE:")
        print("python3 filename.py imagefile")
        return
    imagefile = sys.argv[1]
    data = image_to_data(imagefile)
    predict_digits(data)

if __name__ == '__main__':
    main()
