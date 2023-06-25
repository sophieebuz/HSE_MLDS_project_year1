import pytest
import pandas as pd
from datetime import datetime
from fastapi.testclient import TestClient
from service.main import app
import requests_mock


@pytest.fixture(scope='session')
def client():
    with requests_mock.Mocker() as rm:
        rm.get('http://localhost', json={})
        with TestClient(app) as c:
            yield c


@pytest.fixture(scope="session")
def create_files(tmp_path_factory):
    tmp_path = 'tmp2'
    fn = tmp_path_factory.mktemp(tmp_path, numbered=False)
    (fn / 'test.csv').touch()
    file_name = str(fn) + '/test.csv'
    df_tmp = pd.DataFrame(
        {'date': [datetime(2023, 6, 20), datetime(2023, 6, 21)],
         'url': ['google.com', 'google.com'],
         'topic': ['Россия', 'Россия'],
         'tags': ['Все', 'Все'],
         'title': ["Фрукты", "Книги"],
         'text': ["Я ем яблоки и груши", "Он любит читать книги"]
         })
    df_tmp.to_csv(file_name, index=False)
    yield fn


def test_create_pred(create_files, client):
    with open(str(create_files) + '/test.csv', 'rb') as f:
        response = client.post("/prediction", files={"uploaded_file": ("test.csv", f)})
        assert response.status_code == 200


def test_create_pred_result(create_files, client):
    with open(str(create_files) + '/test.csv', 'rb') as f:
        response = client.post("/prediction", files={"uploaded_file": ("test.csv", f)})
        assert response.status_code == 200
        assert b'Prediction' in response.content


# def test_analysing(client):
#     res = client.get("/analyse_text?name=test&pr=0")
    # print(res)
    # print(res.return_value)
    # response = client.get("/analyse_text?name=test&pr=0")
    # assert res.status_code == 200


# def test_doing_predictions():
#     file_path = 'test.csv'
#     file_path_preprocessed = f'{file_path}_preprocessed'
#     y_pred, num = doing_predictions(file_path, file_path_preprocessed)
#     assert isinstance(y_pred, list)
#     assert isinstance(num, int)
