# importing the required libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action = 'ignore')
# reading the dataset
df = pd.read_csv("static/Crop_recommendation.csv")

non_zero_list = np.count_nonzero(df,axis=0)

for i in range(len(df.columns)):
    print(df.columns[i],len(df)-non_zero_list[i])

k=df.corr()
print(k)
corr_list = [[i,j] for i in k for j in k if i!=j and abs(k[i][j])>0.5]

x=df.drop(columns=["label"])
y=df["label"]
# printing to look the head of the data set
print(x.head())
print(y.head())
# splitting the data into training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=100)
# importing the algorithms
from sklearn.ensemble import RandomForestClassifier as RFC
classifierRFC = RFC()

from sklearn.tree import DecisionTreeClassifier as DTC
classifierDTC = DTC()
# fit and predicting the models
classifierRFC.fit(x_train,y_train)
classifierDTC.fit(x_train,y_train)

predictDTC = classifierDTC.predict(x_test)
predictRFC = classifierRFC.predict(x_test)

print(classifierRFC.score(x_test,y_test),"rfc score")
print(classifierDTC.score(x_test,y_test),"dtc score")

# generating the classification report
from sklearn.metrics import classification_report
yup = classification_report(y_test,predictDTC)
print("========================")
print("Classification report DTC")
print(yup)
print("========================")
dtc = classification_report(y_test,predictRFC)
print("========================")
print("Classification report RFC")
print(dtc)
print("========================")
x_t = np.array([[90,42,43,20.6,82.3,6.4,204.1]])

p=classifierRFC.predict(x_t)
print(p[0])
# dumping the file
import pickle
pickle.dump(classifierRFC,open("model.pkl","wb"))
