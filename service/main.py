import os
import pandas as pd
from fastapi import FastAPI, File, HTTPException, Request, UploadFile, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from service.db_api import db_api
from service.analysing import (count_topics, count_unigrams, draw_wordcloud,
                               text_print)
from service.utils import doing_predictions
import io
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware
from service.metrics import REQUESTS, REQUESTS_LATENCY
from prometheus_client import generate_latest, multiprocess, CollectorRegistry, CONTENT_TYPE_LATEST


app = FastAPI()
app.mount("/static", StaticFiles(directory="./service/static"), name="static")
templates = Jinja2Templates(directory="./service/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root(request: Request):
    REQUESTS.labels(route="root").inc()
    return templates.TemplateResponse('main_page.html',
                                      {"request": request})


@app.get("/upload_file")
async def upload(request: Request):
    with REQUESTS_LATENCY.labels(route="upload_file").time():
        REQUESTS.labels(route="upload_file").inc()
        return templates.TemplateResponse('upload_file.html',
                                        {"request": request})


@app.post("/prediction")
async def create_pred(request: Request,
                      uploaded_file: UploadFile = File(...)):
    csv_name = uploaded_file.filename
    assert csv_name
    csv = io.StringIO(uploaded_file.file.read().decode())
    df = pd.read_csv(csv)

    try:
        y_pred, num = doing_predictions(df, csv_name)
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
                                       "csv_name": csv_name,
                                       "picture": picture})


@app.get("/analyse_text")
async def analysing(request: Request):
    params = dict(request.query_params)
    csv_name = params['name']
    db = db_api()
    df = db.get_df(table='preprocessed_texts', csv_name=csv_name)
    df.rename(columns={'texts': 'text'}, inplace=True)
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
