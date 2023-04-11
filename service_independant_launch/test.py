import pandas as pd
import numpy as np
from feature_engineering import make_date_features
from lemmatization import lemmatization
from model import COLUMNS, load_model


def doing_test(path: str):
    df = pd.read_csv(f"./{path}")
    if set(df.columns) != {'date', 'url', 'topic', 'tags', 'title', 'text'}:
        raise NameError("Несоответствие формата таблицы")

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    lemmatization(df)
    make_date_features(df)
    df.to_csv('static/lib/df_preprocess.csv', index=False)

    clf = load_model("./picke_files/catboost.pkl")
    label_encoder = load_model("./picke_files/labelencoder.pkl")
    y_pred = np.ravel(clf.predict(df[COLUMNS]))

    dict_topic = dict(zip(np.arange(0, len(label_encoder.classes_)),
                          label_encoder.classes_))
    preds = [dict_topic[i] for i in y_pred]
    num = np.arange(0, len(preds))

    return preds, num
