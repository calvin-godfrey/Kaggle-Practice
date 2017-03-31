import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV
from sklearn.feature_extraction import DictVectorizer

data = pd.read_csv("train.csv", index_col=0)

x = data[["Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]]
y = data.Survived

k_range = range(1, 31)
param_grid = dict(n_neighbors=k_range)
print x
print x.to_dict()
#knn = KNeighborsClassifier()
#print cross_val_score(knn, x, y, cv=10, scoring="accuracy")
#grid = GridSearchCV(knn, param_grid, cv=10, scoring="accuracy")
