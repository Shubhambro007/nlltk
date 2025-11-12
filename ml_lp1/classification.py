import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

def decision_tree(filepath, target_col):
    df = pd.read_csv(filepath)
    X = pd.get_dummies(df.drop(columns=[target_col]), drop_first=True)
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test)))

def naive_bayes(filepath, target_col):
    df = pd.read_csv(filepath)
    X = pd.get_dummies(df.drop(columns=[target_col]), drop_first=True)
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = GaussianNB()
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test)))
