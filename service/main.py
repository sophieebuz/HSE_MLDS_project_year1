import pandas as pd
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from test import doing_test
from analysing import text_print, draw_wordcloud, count_unigrams, count_topics
import os


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


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
                      uploaded_file: UploadFile=File(...)):
    csv_name = uploaded_file.filename
    file_path = f'static/lib/{csv_name}'
    with open(file_path, mode='wb+') as f:
        f.write(uploaded_file.file.read())

    y_pred, num = doing_test(file_path)
    print("ok")
    picture = count_topics(y_pred)
    print("ok5")

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
    path=f'static/lib/{csv_name}'
    news = text_print(path=path,i=params['pr'])
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
