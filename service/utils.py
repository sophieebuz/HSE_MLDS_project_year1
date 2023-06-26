import numpy as np
import pandas as pd

from final_pipeline.feature_engineering import encoder, make_date_features
from final_pipeline.lemmatization import lemmatization
from final_pipeline.model import COLUMNS, load_model

clf, label_encoder = load_model(
    model_pickle_file="./final_pipeline/data/catboost.pkl",
    label_encoder_pickle_file="./final_pipeline/data/labelencoder.pkl"
)


def doing_predictions(file_path: str, file_path_preprocessed: str):
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")
    lemmatization(df)
    make_date_features(df)

    for required_column in COLUMNS:
        if required_column not in df.columns:
            raise NameError(f"Несоответствие формата таблицы, нет колонки {required_column}")

    # encoder(df, label_encoder)
    y_pred = np.ravel(clf.predict(df[COLUMNS]))

    df.to_csv(file_path_preprocessed, index=False)

    dict_topic = dict(zip(np.arange(0, len(label_encoder.classes_)), label_encoder.classes_))
    preds = [dict_topic[i] for i in y_pred]
    num = np.arange(0, len(preds))
    return preds, num
