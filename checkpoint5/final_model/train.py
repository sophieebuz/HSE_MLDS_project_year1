import pandas as pd

from feature_engineering import encoder, make_date_features
from lemmatization import lemmatization
from model import train_model


def clean_train_data(df):
    df = df[df["date"].dt.year != 1914]

    df = df[~df["text"].isna()]

    classes_to_drop = ["Библиотека", "Оружие", "ЧМ-2014",
                       "Мотор", "МедНовости", "Сочи"]
    df = df[(~df["topic"].isna()) & (~df["topic"].isin(classes_to_drop))]
    return df


if __name__ == "__main__":
    df = pd.read_csv("train.csv")

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df = clean_train_data(df)

    lemmatization(df)
    encoder(df)
    make_date_features(df)

    clf = train_model(df, df['topic_le'])

