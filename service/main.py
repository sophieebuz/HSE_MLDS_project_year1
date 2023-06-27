import os
import pandas as pd
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from service.db_api import db_api
from service.analysing import (count_topics, count_unigrams, draw_wordcloud,
                               text_print)
from service.utils import doing_predictions
from service.monitoring import get_blocks
import datetime
import platform
import psutil


app = FastAPI()
app.mount("/static", StaticFiles(directory="./service/static"), name="static")
templates = Jinja2Templates(directory="./service/templates")

@app.get("/monitoring")
async def monitoring(request: Request):
    active_since = datetime.datetime.fromtimestamp(psutil.boot_time())
    return templates.TemplateResponse("monitoring.html",
                           {"request": request,
                            'script_version':'1.0.0',
                           'active_since':active_since,
                           'days_active':(datetime.datetime.now() - active_since).days,
                           'system':platform.system(),
                           'release':platform.release(),
                           'version':platform.version(),
                           'blocks':get_blocks()})


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
    db = db_api()
    table = db.push_csv(uploaded_file=uploaded_file)

    try:
        y_pred, num = doing_predictions(table)
    except NameError as exception:
        print(exception)
        raise HTTPException(status_code=500, detail=str(exception))
    except ValueError as exception:
        print(exception)
        raise HTTPException(
            status_code=500,
            detail="Что то пошло не так. Проверьте соответствие формата входного файла. Попробуйте снова..."
        )

    picture = count_topics(y_pred)

    return templates.TemplateResponse('prediction.html',
                                      {"request": request,
                                       "pred": y_pred,
                                       "num": num,
                                       "csv_name": table,
                                       "picture": picture})


@app.get("/analyse_text")
async def analysing(request: Request):
    params = dict(request.query_params)
    csv_name = params['name']
    db = db_api()
    df = db.get_df(table=f'{csv_name}_preprocessed')
    news = text_print(df=df, i=params['pr'])
    wcloud = draw_wordcloud(df=df, i=params['pr'], photo=False)
    unigrams = count_unigrams(df=df, i=params['pr'])

    return templates.TemplateResponse('analyse_text.html',
                                      {"request": request,
                                       "title": news['title'],
                                       "text": news['text'],
                                       "date": news['date'],
                                       "url": news['url'],
                                       "wcloud": wcloud,
                                       "picture": unigrams})
