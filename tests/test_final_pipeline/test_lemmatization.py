import pandas as pd
from final_pipeline.lemmatization import lemmatization


def test_lemmatization():
    df = pd.DataFrame({
        "text": ["Я ем яблоки и груши", "Он любит читать книги"],
        "title": ["Фрукты", "Книги"]
    })
    expected_output = pd.DataFrame({
        "text_str": ["яблоко груша", "любить читать книга"],
        "title_lemmas": ["фрукт", "книга"]
    })
    expected_output = pd.concat([df, expected_output], axis=1)
    lemmatization(df)
    pd.testing.assert_frame_equal(df, expected_output)


def test_lemmatization_parallel():
    df = pd.DataFrame({
        "text": ["Я ем яблоки и груши", "Он любит читать книги"],
        "title": ["Фрукты", "Книги"]
    })
    expected_output = pd.DataFrame({
        "text_str": ["яблоко груша", "любить читать книга"],
        "title_lemmas": ["фрукт", "книга"]
    })
    expected_output = pd.concat([df, expected_output], axis=1)
    lemmatization(df, True)
    pd.testing.assert_frame_equal(df, expected_output)
