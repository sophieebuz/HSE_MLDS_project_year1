# import os
# import pickle
# import pandas as pd
# from catboost import CatBoostClassifier
# from sklearn.preprocessing import LabelEncoder
# from final_pipeline.model import train_model, load_model, save_model


# def test_train_model():
#     X = pd.DataFrame({
#         "text_str": ["яблоко груша", "любить читать книга"],
#         "title_lemmas": ["фрукт", "книга"],
#         "date_enc": [1, 2],
#         "year": [2020, 2021],
#         "season": [1, 1],
#         "day_of_week": [1, 0]
#     })
#     y = pd.Series([0, 1])
#     model = train_model(X, y)
#     assert isinstance(model, CatBoostClassifier)


# def test_save_and_load_model():
#     X = pd.DataFrame({
#         "text_str": ["Я люблю котиков", "Он любит собак"],
#         "title_lemmas": ["Кошки", "Собаки"],
#         "date_enc": [1, 2],
#         "year": [2020, 2021],
#         "season": ["winter", "summer"],
#         "day_of_week": ["Monday", "Friday"]
#     })
#     y = pd.Series([0, 1])
#     model = train_model(X, y)
#     label_encoder = LabelEncoder()
#     label_encoder.fit(y)
#     model_pickle_file = "model.pkl"
#     label_encoder_pickle_file = "label_encoder.pkl"
#     save_model(model_pickle_file, model, label_encoder_pickle_file, label_encoder)
#     loaded_model, loaded_label_encoder = load_model(model_pickle_file, label_encoder_pickle_file)
#     assert isinstance(loaded_model, CatBoostClassifier)
#     assert isinstance(loaded_label_encoder, LabelEncoder)
#     os.remove(model_pickle_file)
#     os.remove(label_encoder_pickle_file)
