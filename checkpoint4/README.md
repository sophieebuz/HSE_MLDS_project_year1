Ссылка на pickle файлы: https://drive.google.com/drive/folders/1XDn1f6sMOvb_X2Yv93xFN2OFoqm1ylZB?usp=share_link


Для решения задачи классификации попробовали 3 модели:

1) [Logistic Regression](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/main/checkpoint4/ML_models_logreg.ipynb)
2) [Random Forest](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/main/checkpoint4/ML_models_random_forest.ipynb)
3) [Catboost](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/main/checkpoint4/ML_models_catboost_experiments.ipynb)

### Логистическая регрессия

Лучшая модель была обучена на униграммах (TF-IDF) 
с добавлением признака сезонности и года (закодированные через OneHotEncoding)

Лучшее качество по метрике f1-micro = 0.844 (гиперпараметр C = 4)