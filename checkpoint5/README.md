Ссылка на pickle файлы: https://drive.google.com/drive/folders/1XDn1f6sMOvb_X2Yv93xFN2OFoqm1ylZB?usp=share_link  
Ссылка на датасет: https://drive.google.com/file/d/1Z32axT_xJUG-VesZiZ4dBVOL2Apafu3e/view?usp=share_link

Содержание папки:
 - Попытки улучшения модели catboost:
   * подбор гиперпарметров с помощью библиотеки optuna `ML_catboost_optuna.ipynb`
   * получение финального прогноза с помощью обучения 2х моделей (для малочисленных и многочисленных классов) `ML_catboost_2models.ipynb`

Оба эти подхода не дали прироста в качестве, поэтому они не были применены ко всему датасету. 

 - Финальная версия модели catboost, обученная на всех данных `ML_models_catboost_fulldf_final_GPU.ipynb`
 
   | Метрика | train | test |
   | ------------- |:------------------:| :-----:|
   | `f1-score 'micro'`| `0.923` | `0.887` |
