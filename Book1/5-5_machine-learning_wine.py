from sklearn import model_selection, svm, metrics

wine_csv = []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
    no = 0
    for line in fp:
        line = line.strip()
        cols = line.split(";")
        wine_csv.append(cols)

wine_csv = wine_csv[1:]

labels = []
data = []
for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols))

    grade = int(cols[11])
    if grade == 9: grade = 8
    if grade < 4: grade = 5
    labels.append(grade)
    data.append( cols[0:11] )

data_train, data_test, label_train, label_test = \
    model_selection.train_test_split(data, labels)

clf = svm.SVC()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート=\n", cl_report)
