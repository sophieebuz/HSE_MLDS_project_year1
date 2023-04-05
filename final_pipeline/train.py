import os

import pandas as pd
from feature_engineering import encoder, make_date_features
from lemmatization import lemmatization
from model import save_model, train_model


def clean_train_data(df):
    df = df[df["date"].dt.year != 1914]

    df = df[~df["text"].isna()]

    classes_to_drop = ["Библиотека", "Оружие", "ЧМ-2014",
                       "Мотор", "МедНовости", "Сочи"]
    df = df[(~df["topic"].isna()) & (~df["topic"].isin(classes_to_drop))]
    return df


if __name__ == "__main__":
    if os.path.exists("./data/catboost.pkl"):
        print("Model file already exists, remove it before run this file")
        exit()

    df = pd.read_csv("./data/train_200k.csv")

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df = clean_train_data(df)

    lemmatization(df)
    label_encoder = encoder(df)
    make_date_features(df)

    clf = train_model(df, df["topic_le"])
    save_model(
        model_pickle_file="./data/catboost.pkl",
        model=clf,
        label_encoder_pickle_file="./data/labelencoder.pkl",
        label_encoder=label_encoder
    )
