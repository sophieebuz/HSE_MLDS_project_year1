import pandas as pd
import pytest
from datetime import datetime
from service.analysing import draw_wordcloud, count_unigrams, count_topics


@pytest.fixture(scope="session")
def create_files(tmp_path_factory):
    tmp_path = 'tmp'
    fn = tmp_path_factory.mktemp(tmp_path, numbered=False)
    (fn / 'test.csv').touch()
    file_name = str(fn) + '/test.csv'
    df_tmp = pd.DataFrame(
        {'date': [datetime(2023, 6, 20), datetime(2023, 6, 21)],
         'url': ['google.com', 'google.com'],
         'topic': ['Россия', 'Россия'],
         'tags': ['Все', 'Все'],
         'title': ["Фрукты", "Книги"],
         'text': ["Я ем яблоки и груши", "Он любит читать книги"],
         'text_str': ["яблоко груша", "любить читать книга"],
         'title_lemmas': ["фрукт", "книга"]
         })
    df_tmp.to_csv(file_name, index=False)
    yield fn


def test_draw_wordcloud(create_files):
    path = str(create_files) + "/test.csv"
    i = "0"
    photo = True
    name = "test_image.png"

    result = draw_wordcloud(path, i, photo, name)

    assert isinstance(result, str)
    assert len(result) > 0


def test_count_unigrams(create_files):
    path = str(create_files) + "/test.csv"
    i = "0"

    result = count_unigrams(path, i)

    assert isinstance(result, str)
    assert len(result) > 0


def test_count_topics():
    topics = ["topic1", "topic2", "topic1", "topic3", "topic2"]

    result = count_topics(topics)

    assert isinstance(result, str)
    assert len(result) > 0
