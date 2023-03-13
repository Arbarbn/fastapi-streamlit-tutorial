
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
import pickle
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/Iris.csv')

# Dropping the Id column
df.drop('Id', axis = 1, inplace = True)

# Renaming the target column into numbers to aid training of the model
df['Species']= df['Species'].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

# splitting the data into the columns which need to be trained(X) and the target column(y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# splitting data into training and testing data with 30 % of data as testing data respectively
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# importing the random forest classifier model and training it on the dataset
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# predicting on the test dataset
y_pred = classifier.predict(X_test)

# finding out the accuracy
score = accuracy_score(y_test, y_pred)

# pickling the model
pickle_out = open("model/classifier.pkl", "wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()




