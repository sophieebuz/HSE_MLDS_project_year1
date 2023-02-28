Ссылка на pickle файлы: https://drive.google.com/drive/folders/1XDn1f6sMOvb_X2Yv93xFN2OFoqm1ylZB?usp=share_link

## Что было сделано?
* Разведочный анализ данных
* Подготовка и кодировка данных
* Визуализация данных
* Классификация текстов по темам при помощи ML моделей:

    - [Logistic Regression](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/main/checkpoint4/ML_models_logreg.ipynb)
    - [Random Forest](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/main/checkpoint4/ML_models_random_forest.ipynb)
    - [Catboost](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/main/checkpoint4/ML_models_catboost_experiments.ipynb)

## Результаты

Метрика качества: f1-micro

| Название | Лучшее качество на тестовой выборке | Время обучения на 200К объектах  | Лучшие гиперпараметры |
| ------------- | ------------- | ------------- | ------------- |
| Random Forest | 0.73 | ~ 35мин.(испол.доп. памяти в Google colab)<br/>  1.5 - 2 ч. (станд.кол-во памяти)| max_depth=60 <br/> n_estimators = 400|
| Logistic Regression |0.844 |~ 20 мин. | C = 4 |
| **Catboost** | **0.877**| **\~ 2 мин.**| **n_estimators = 1600** |

## Наилучшая модель Catboost включила в себя:

**признаки:**<br/> 
  - text_str - лемматизированный текст новостей<br/> 
  - title_lemmas - лемматизированные заголовки<br/> 
  - date_enc - закодированная дата (подробнее о кодировке см. ML_model_catboost.ipybn )<br/> 
  - year - год<br/> 
  - season - время загода (подробнее о кодировке см. ML_model_catboost.ipybn )<br/> 
  - day_of_week - день недели (подробнее о кодировке см. ML_model_catboost.ipybn )<br/> 
  
  **оптимальные гиперпараметры:**
  - n_estimators=1600 - кол-во деревьев<br/> 
  - depth=9 - глубина деревьев<br/> 
  - learning rate подбирался самим алгоритмом катбуста<br/> 
