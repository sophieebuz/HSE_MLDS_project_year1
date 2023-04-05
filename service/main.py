from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from service.analysing import (count_topics, count_unigrams, draw_wordcloud,
                               text_print)
from service.utils import doing_predictions

app = FastAPI()
app.mount("/static", StaticFiles(directory="./service/static"), name="static")
templates = Jinja2Templates(directory="./service/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('main_page.html',
                                      {"request": request})


@app.get("/upload_file")
async def upload(request: Request):
    return templates.TemplateResponse('upload_file.html',
                                      {"request": request})


@app.post("/prediction")
async def create_pred(request: Request,
                      uploaded_file: UploadFile = File(...)):
    csv_name = uploaded_file.filename
    assert csv_name

    file_path = f'./service/static/lib/{csv_name}'
    with open(file_path, mode='wb+') as f:
        f.write(uploaded_file.file.read())

    try:
        y_pred, num = doing_predictions(file_path)
    except NameError as exception:
        print(exception)
        raise HTTPException(status_code=404, detail=str(exception))
    except ValueError as exception:
        print(exception)
        raise HTTPException(
            status_code=404,
            detail="Что то пошло не так. Проверьте соответствие формата входного файла. Попробуйте снова..."
        )

    picture = count_topics(y_pred)

    return templates.TemplateResponse('prediction.html',
                                      {"request": request,
                                       "pred": y_pred,
                                       "num": num,
                                       "csv_name": csv_name,
                                       "picture": picture})


@app.get("/analyse_text")
async def analysing(request: Request):
    params = dict(request.query_params)
    csv_name = params['name']
    path = f'static/lib/{csv_name}'
    news = text_print(path=path, i=params['pr'])
    wcloud = draw_wordcloud(i=params['pr'], photo=False)
    unigrams = count_unigrams(i=params['pr'])

    return templates.TemplateResponse('analyse_text.html',
                                      {"request": request,
                                       "title": news['title'],
                                       "text": news['text'],
                                       "date": news['date'],
                                       "url": news['url'],
                                       "wcloud": wcloud,
                                       "picture": unigrams})
