# Анализ тональности и внутренней структуры текстов новостей

### Команда

| Имя | Телеграмм |
| ------ | ------ |
| Бузаева Софья | [@ethee_real](https://t.me/ethee_real) |
| Иванцова Анна | [@unclebensico](https://t.me/unclebensico) |
| Кучумова Милана | [@milana_kma](https://t.me/milana_kma) |
| Шикина Евгения | [@JaneShikina](https://t.me/JaneShikina) |

### Описание проекта
В данном проекте анализируются новости с сайта [Lenta.ru](https://www.kaggle.com/datasets/yutkin/corpus-of-russian-news-articles-from-lenta?resource=download) при помощи различных методов машинного и глубинного обучения на текстовых данных.

[Датасет до 2022](https://drive.google.com/file/d/1nGpqnw9pUCq0_hvZDDluAeRlbe_rm0WK/view?usp=sharing)

[Датасет с обработкой pymorphy2](https://drive.google.com/file/d/1RI1pSHTxX7SyZ6ypKGkrHM-HfGsndXrr/view?usp=share_link)

[Датасет с обработкой pymystem3](https://drive.google.com/file/d/15eUU2kvFs4ZkbX6wbuT55UfYSQfpRR5L/view?usp=sharing)


### Запуск всего приложения (с базой данных и мониторингом)
```
docker-compose up --build
```

### Запуск  проекта
```
make init
python final_pipeline/train.py
python final_pipeline/test.py
```

### Запуск web-сервиса локально
```
make init
make run_service
```
открыть в браузере страницу  http://127.0.0.1:8000

### Запуск web-сервиса внутри докер контейнера
```
make download_data
make -i docker_build
make docker_start
```

### Запуск web-сервиса c помощью докер-образ проекта на Dockerhub

https://hub.docker.com/repository/docker/annaivantsova/hse_mlds_project_year1_service/general

```
docker run --rm -it --name mlds_project_year1_service -p 8000:8000 annaivantsova/hse_mlds_project_year1_service
```