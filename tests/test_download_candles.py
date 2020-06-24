import pytest
import pandas as pd
from xchg import download_sample


@pytest.fixture
def test_candles():
  return list(
    [
      {
        'date': 1575158400,
        'high': 0.02009497,
        'low': 0.020021,
        'open': 0.02007299,
        'close': 0.02008,
        'volume': 2.83754783,
        'quoteVolume': 141.51364588,
        'weightedAverage': 0.0200514
      },
      {
        'date': 1575160200,
        'high': 0.02014813,
        'low': 0.02007299,
        'open': 0.02008427,
        'close': 0.02012469,
        'volume': 0.15556988,
        'quoteVolume': 7.73633777,
        'weightedAverage': 0.02010898
      }
    ]
  )


@pytest.fixture
def test_dataframe():
  d = dict(
    {
      'date': [1575158400, 1575160200],
      'high': [0.02009497, 0.02014813],
      'low': [0.020021, 0.02007299],
      'open': [0.02007299, 0.02008427],
      'close': [0.02008, 0.02012469],
      'volume': [2.83754783, 0.15556988],
      'quoteVolume': [141.51364588, 7.73633777],
      'weightedAverage': [0.0200514, 0.02010898]
    }
  )
  return pd.DataFrame(data=d).set_index('date')


def test_request(test_candles):
  '''Test request to Poloniex.'''
  candles = download_sample.request('ETH', 1800, 1575158400, 1575160200)
  assert candles == test_candles


def test_candles_to_df(test_candles, test_dataframe):
  '''Test conversion from candles to Pandas DataFrame.'''
  assert download_sample.candles_to_df(test_candles) == test_dataframe


def test_request(test_candles):
  '''Test request to Poloniex.'''
  candles = download_sample.request('ETH', 1800, 1575158400, 1575160200)
  assert candles == test_candles
