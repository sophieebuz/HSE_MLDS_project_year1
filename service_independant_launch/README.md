_**Примечание**_ файлы, содержащиеся в данной папке, не являются финальными версиями. Далее код в них будет дорабатываться и улучшаться.


### Описание функционала сервиса.
Данная папка содержит сервис на fastapi, работающий на основании модели, разработанной ранее для тематического моделирования текстов. Сервис имеет пользовательский интерфейс, с которым можно работать из браузера.


> Осуществить запуск микросервиса можно двумя способами:
> - в докер-контейнере из созданного docker-image проекта
> - локально на компьютере
 
 
### Запуск сервиса в докер-контейнере из созданного docker-image проекта
 1. Запустить Docker Desktop
 2. Написать в терминале следующую команду:
    ```
    docker run --rm -it -p 8898:8000 --name mlds_project_year1_service sofibuz/hse_mlds_project_year1_service
    ```
    _Примечание_: [ссылка на dockerhub](https://hub.docker.com/repository/docker/sofibuz/hse_mlds_project_year1_service/general) 
 
### Запуск сервиса локально на компьютере
 1. Скачать содержимое папки `"service_independant_launch"`
 2. Скачать и положить в корень папки `picke_files` слудующие pickle файлы:
    - https://drive.google.com/file/d/1Lr2N4LxsugqyQTzsbxUfJYOgIAokla4i/view?usp=share_link
    - https://drive.google.com/file/d/1tnzoCwZXK6LA_yFv0LEki_cE_53V-kwj/view?usp=share_link
 3. Создать виртуальное окружение с python 3.10  
    _Примечание_: важно, чтобы версия питона была именно эта
 5. Поставьте зависимости для проекта (установить необходимые пакеты для работы сервиса):
    ```
    pip install -r requirements.txt
    ```
 6. Для запуска сервиса в терминале написать команду
    ```
    uvicorn main:app
    ```

### Инструкция по использованию сервиса

![img1](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/main_page_str.jpg)
