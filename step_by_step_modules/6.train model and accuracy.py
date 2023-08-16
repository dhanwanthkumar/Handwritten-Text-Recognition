import pandas as pd 
from sklearn.model_selection import train_test_split
import joblib
from sklearn.svm import SVC

data = pd.read_csv('dataset.csv')
X = data.drop(["label"],axis=1)
Y= data["label"]

train_x,test_x,train_y,test_y = train_test_split(X,Y, test_size = 0.2)


classifier=SVC(kernel="linear", random_state=6)
classifier.fit(train_x,train_y)
joblib.dump(classifier, "model/digit_recognizer")

#calculate accuracy

from sklearn import metrics
prediction=classifier.predict(test_x)
print("Accuracy= ",metrics.accuracy_score(prediction, test_y))