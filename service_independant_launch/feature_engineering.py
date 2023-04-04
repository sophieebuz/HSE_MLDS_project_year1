import typing
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encoder(df: pd.DataFrame, le: typing.Optional[LabelEncoder] = None) -> LabelEncoder:
    if not le:
        le = LabelEncoder()
        le = le.fit(df.topic)
    df["topic_le"] = le.transform(df.topic)
    return le


def make_date_features(df: pd.DataFrame):
    # df.drop("Unnamed: 0", axis=1, inplace=True)
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["date_enc"] = df["year"] * 365 + df["month"] * 30 + df["day"]
    min_date = df.date.min().year * 365 + df.date.min().month * 30 + df.date.min().day
    df["date_enc"] = df["date_enc"] - min_date
    df["day_of_week"] = df["date"].dt.day_of_week

    # Фича по сезону в году
    seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
    month_to_season = dict(zip(range(1, 13), seasons))
    df["season"] = df["month"].map(month_to_season)

    # Фича выходной или нет
    df["dummy_weekday"] = 1
    df.loc[df["day_of_week"] >= 5, "dummy_weekday"] = 0
