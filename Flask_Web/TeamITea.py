import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score

def vorhersage(text):
    text = [text]

    df=pd.read_csv("Flask_Web/GM_Clean.csv")


    Independent_var = df.Bewertung
    Dependent_var = df.Sternebewertung

    IV_train, IV_test, DV_train, DV_test = train_test_split(Independent_var, Dependent_var, test_size = 0.15, random_state = 225)

    tvec = TfidfVectorizer()
    clf2 = LogisticRegression(solver = "lbfgs")

    model = Pipeline([('vectorizer',tvec),('classifier',clf2)])
    model.fit(IV_train, DV_train)

    predictions = model.predict(IV_test)
    confusion_matrix(predictions, DV_test)

    result = model.predict(text)

    return result
