import os
import pickle
import typing

import pandas as pd
from catboost import CatBoostClassifier
from sklearn.preprocessing import LabelEncoder

COLUMNS = ['text_str', 'title_lemmas', 'date_enc', 'year', 'season', 'day_of_week']


def train_model(X: pd.DataFrame, y: pd.DataFrame) -> CatBoostClassifier:
    """
    Функция обучает
    X - матрица "объект-признак"
    y - таргет
    """

    gpu_is_available = False
    try:
        import torch
        gpu_is_available = torch.cuda.is_available()
    except ImportError:
        pass

    text_cols = ['text_str', 'title_lemmas']
    cat_cols = ['year', 'day_of_week', 'season']
    clf = CatBoostClassifier(random_state=123,
                             loss_function='MultiClass',
                             eval_metric='TotalF1',
                             task_type='GPU' if gpu_is_available else 'CPU',
                             n_estimators=1600,
                             depth=9)
    model = clf.fit(X[COLUMNS], y,
                    text_features=text_cols,
                    cat_features=cat_cols)

    return model


def load_model(
        model_pickle_file: str,
        label_encoder_pickle_file: str
) -> typing.Tuple[CatBoostClassifier, LabelEncoder]:
    """
    Функция загружает модель из pickle файла
    """
    with open(model_pickle_file, 'rb') as file:
        model = pickle.load(file)

    with open(label_encoder_pickle_file, 'rb') as file:
        label_encoder = pickle.load(file)

    return model, label_encoder


def save_model(
        model_pickle_file: str,
        model: CatBoostClassifier,
        label_encoder_pickle_file: str,
        label_encoder: LabelEncoder
):
    if os.path.exists(model_pickle_file):
        os.remove(model_pickle_file)

    with open(model_pickle_file, 'wb') as handle:
        pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if os.path.exists(label_encoder_pickle_file):
        os.remove(label_encoder_pickle_file)

    with open(label_encoder_pickle_file, 'wb') as handle:
        pickle.dump(label_encoder, handle, protocol=pickle.HIGHEST_PROTOCOL)
