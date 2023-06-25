import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
from final_pipeline.feature_engineering import encoder, make_date_features


def test_encoder():
    data = {'topic': ['a', 'b', 'c', 'd', 'e', 'f'],
            'value': [1, 2, 3, 4, 5, 6]}
    df = pd.DataFrame(data)
    le = encoder(df)
    assert isinstance(le, LabelEncoder)
    assert np.array_equal(le.transform(df.topic), [0, 1, 2, 3, 4, 5])


def test_make_date_features():
    data = {'date': [datetime(2023, 6, 20), datetime(2023, 6, 21),
                     datetime(2023, 6, 22)], 'value': [1, 2, 3]}
    df = pd.DataFrame(data)
    make_date_features(df)

    expected = pd.DataFrame({'date': [datetime(2023, 6, 20),
                                      datetime(2023, 6, 21),
                                      datetime(2023, 6, 22)],
                             'value': [1, 2, 3],
                             'year': [2023, 2023, 2023],
                             'month': [6, 6, 6],
                             'day': [20, 21, 22],
                             'date_enc': [0, 1, 2],
                             'day_of_week': [1, 2, 3],
                             'season': [3, 3, 3],
                             'dummy_weekday': [1, 1, 1]})
    assert_frame_equal(df, expected)
