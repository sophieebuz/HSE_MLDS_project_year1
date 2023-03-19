from catboost import CatBoostClassifier
import pandas as pd
import pickle


def train_model(X: pd.DataFrame, y: pd.DataFrame) -> CatBoostClassifier:
    """
    Функция обучает
    X - матрица "объект-признак"
    y - таргет
    """

    cols = ['text_str', 'title_lemmas', 'date_enc', 'year', 'season',
            'day_of_week']
    text_cols = ['text_str', 'title_lemmas']
    cat_cols = ['year', 'day_of_week', 'season']
    clf = CatBoostClassifier(random_state=123,
                             loss_function='MultiClass',
                             eval_metric='TotalF1',
                             task_type='GPU',
                             n_estimators=1600,
                             depth=9)
    model = clf.fit(X[cols], y,
                    text_features=text_cols,
                    cat_features=cat_cols)

    return model


def load_model(pickle_file: str = "pickle_model_catboost_final_gpu90%.pkl"):
    """
    Функция загружает модель из pickle файла
    """

    columns = ['text_str', 'title_lemmas', 'date_enc', 'year', 'season',
               'day_of_week']
    with open(pickle_file, 'rb') as file:
        model = pickle.load(file)
    return model, columns
