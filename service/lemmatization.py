import nltk
import pandas as pd
from nltk.corpus import stopwords
#from pandarallel import pandarallel
from pymystem3 import Mystem

nltk.download("stopwords")

#pandarallel.initialize(progress_bar=True)


def make_lemmas(text: str, mystem_instance: Mystem) -> str:
    """
    Лемматизируем строку, проверяя следующие моменты:
        - не стоп-слово
        - длина больше 2х символов
        - состоит только из букв или слова, которые пишутся через тире
    """
    stopwords_rus = stopwords.words("russian")
    text = str(text)
    lemmas = mystem_instance.lemmatize(text)
    text_splitted = [
        i.lower()
        for i in lemmas
        if i not in stopwords_rus
        and len(i) > 2
        and (i.isalpha() or ((i.split("-")[0]).isalpha()))
    ]
    return " ".join(text_splitted)


def lemmatization(df: pd.DataFrame):
    mystem_instance = Mystem()
    lemmas_text = [make_lemmas(df['text'][i], mystem_instance) for i in range(len(df))]
    lemmas_title = [make_lemmas(df['title'][i], mystem_instance) for i in range(len(df))]
    df['text_str'] = lemmas_text
    df['title_lemmas'] = lemmas_title

    #df['text_str'] = df["text"].parallel_apply(make_lemmas, args=[mystem_instance])
    #df['title_lemmas'] = df["title"].parallel_apply(make_lemmas, args=[mystem_instance])
