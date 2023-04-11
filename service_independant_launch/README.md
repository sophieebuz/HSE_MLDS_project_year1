### Описание функционала сервиса.
Данная папка содержит сервис на fastapi, работающий на основании разработанной ранее модели для тематического моделирования текстов. Сервис имеет пользовательский интерфейс, с которым можно работать из браузера.  
Более детальные инструкции по работе сервиса можно найти в разделе "Инструкция по использованию сервиса".


> Осуществить запуск микросервиса можно двумя способами:
> - в докер-контейнере из созданного docker-image проекта
> - локально на компьютере с помощью Poetry
> - локально на компьютере через requirements.txt
 
 
### Запуск сервиса в докер-контейнере из созданного docker-image проекта
 1. Запустить Docker Desktop
 2. Написать в терминале следующую команду:
    ```
    docker run --rm -it -p 8898:8000 --name mlds_project_year1_service sofibuz/hse_mlds_project_year1_service
    ```
    _Примечание_: [ссылка на dockerhub](https://hub.docker.com/repository/docker/sofibuz/hse_mlds_project_year1_service/general) 


### Запуск сервиса локально на компьютере с помощью Poetry
 1. Скачать содержимое папки `"service_independant_launch"`
 2. Скачать и положить в корень папки `picke_files` слудующие pickle файлы:
    - https://drive.google.com/file/d/1Lr2N4LxsugqyQTzsbxUfJYOgIAokla4i/view?usp=share_link
    - https://drive.google.com/file/d/1tnzoCwZXK6LA_yFv0LEki_cE_53V-kwj/view?usp=share_link
 3. Для установки виртуальной среды в терминале написать команду (предварительно убедитель, что утилита Poetry у вас стоит) 
    ```
    poetry install
    ```
 4. Для запуска сервиса в терминале написать команду
    ```
    poetry run uvicorn main:app
    ```


### Запуск сервиса локально на компьютере через requirements.txt
 1. Скачать содержимое папки `"service_independant_launch"`
 2. Скачать и положить в корень папки `picke_files` слудующие pickle файлы:
    - https://drive.google.com/file/d/1Lr2N4LxsugqyQTzsbxUfJYOgIAokla4i/view?usp=share_link
    - https://drive.google.com/file/d/1tnzoCwZXK6LA_yFv0LEki_cE_53V-kwj/view?usp=share_link
 3. Создать виртуальное окружение с python 3.10  
    _Примечание_: важно, чтобы версия питона была именно эта
 4. Поставьте зависимости для проекта (установить необходимые пакеты для работы сервиса):
    ```
    pip install -r requirements.txt
    ```
 5. Для запуска сервиса в терминале написать команду
    ```
    uvicorn main:app
    ```

### Инструкция по использованию сервиса
 1. После того как приложение будет запущено перейдите в браузер и перейдите по следующему url:
     - `http://localhost:8898/` (при запуске из докер-контейнера)
     - `http://127.0.0.1:8000/` (при локальном запуске)  
     Вы попадете на главную страницу. Для дальнейшей работы кликните на "перейти к загрузке файла".

 ![img1](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/main_page_str.jpg)

 2. Вам будет предложено загрузить csv файл для получения предсказаний.  
    Файл должен содержать следующие столбцы, значение которых разделено запятой. 
    | date | url | topic | tags | title | text |
    | ------ | ------ | ------ | ------ | ------ | ------ |
    | гггг/мм/дд | url ссылка | тема статьи | "подтема" статьи | заголовок статьи | текст статьи |
    | 2021/08/16 | https://lenta.ru/news/2021/08/16/anomalii/ | Россия | Общество | Синоптик рассказал | "Аномально теплая погода на территории России." |
    
    Пример csv файла:
 ![img2_0](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/example_of_csv_file.jpg)
 
 ![img2](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/uploadfile1_str.jpg)

 3. После успешной загрузки файла справа от кнопки "Выберите файл" появится надпись, показывающая название загруженного файла.  
    Нажмите на кнопку "Отправить". Далее подождите пока ваши данные будут обрабаываться.
 ![img3](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/uploadfile2_str.jpg)

 4. Вы увидите предсказания, полученные на основе модели. Справа будет изображен график, показывающий распределение по темам загруженных текстов, т.е. сколько раз встретилась среди предсказаний конкретная тема.  
    При желании получить более детальную информацию по каждому из загруженных текстов нажмите на предсказанную тему, соответствующую номеру текста.
 ![img4](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/prediction.jpg)
 
  5. После перехода вы увидите более детальную информацию о выбранном тексте.
  ![img5](https://github.com/sophieebuz/HSE_MLDS_project_year1/blob/service_independant_launch/service_independant_launch/screenshots/analyse_text.jpg)
 
