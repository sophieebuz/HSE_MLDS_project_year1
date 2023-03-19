import pandas as pd

from feature_engineering import make_date_features
from lemmatization import lemmatization
from model import load_model

if __name__ == "__main__":
    df = pd.read_csv("test.csv")

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    lemmatization(df)
    make_date_features(df)

    clf, cols = load_model()
    y_pred = clf.predict(df[cols])
