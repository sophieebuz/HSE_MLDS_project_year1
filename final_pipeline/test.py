import pandas as pd
from feature_engineering import encoder, make_date_features
from lemmatization import lemmatization
from model import COLUMNS, load_model
from sklearn.metrics import classification_report, f1_score

if __name__ == "__main__":
    df = pd.read_csv("./final_pipeline/data/test_50k.csv")

    df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")
    lemmatization(df)
    make_date_features(df)

    clf, label_encoder = load_model(
        model_pickle_file="./final_pipeline/data/catboost.pkl",
        label_encoder_pickle_file="./final_pipeline/data/labelencoder.pkl"
    )
    encoder(df, label_encoder)
    y_pred = clf.predict(df[COLUMNS])

    dict_topic = dict(zip(df.topic, df.topic_le))
    dict_topic = dict(sorted(dict_topic.items(), key=lambda item: item[1]))
    print(classification_report(df["topic_le"], y_pred, target_names=dict_topic, zero_division=0))

    total_score = f1_score(df["topic_le"], y_pred.ravel(), average="weighted", zero_division=0)
    print(f"Total score: {total_score}")
