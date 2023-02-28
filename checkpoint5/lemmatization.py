import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
from pandarallel import pandarallel
from pymystem3 import Mystem

pandarallel.initialize(progress_bar=True)


def make_lemmas(x, m):
    """
    Лемматизируем строку, проверяя следующие моменты:
        - не стоп-слово
        - длина больше 2х символов
        - состоит только из букв или слова, которые пишутся через тире
    """
    stopwords_rus = stopwords.words("russian")
    x = str(x)
    lemmas = m.lemmatize(x)
    text = [
        i.lower()
        for i in lemmas
        if i not in stopwords_rus
        and len(i) > 2
        and (i.isalpha() or ((i.split("-")[0]).isalpha()))
    ]
    return " ".join(text)


def lemmatization(df, column_name):
    m = Mystem()
    df[column_name] = df[column_name].parallel_apply(make_lemmas, args=[m])
    return df
