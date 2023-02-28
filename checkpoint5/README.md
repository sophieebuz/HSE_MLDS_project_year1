Ссылка на pickle файлы: https://drive.google.com/drive/folders/1XDn1f6sMOvb_X2Yv93xFN2OFoqm1ylZB?usp=share_link

Содержание папки:
 - попытки улучшения модели catboost:
   * подбор гиперпарметров с помощью библиотеки optuna `ML_catboost_optuna.ipynb`
   * получение финального прогноза с помощью обучения 2х моделей (для малочисленных и многочисленных классов) `ML_catboost_2models.ipynb`

Оба эти подхода не дали прироста в качестве, поэтому они не были применены ко всему датасету. 

 - финальная версия модели, обученная на всех данных `ML_models_catboost_fulldf_final_GPU.ipynb`

 Метрика | train | test |
    | ------------- |:------------------:| :-----:|
    | `f1-score 'micro'`| `0.923` | `0.887` |
