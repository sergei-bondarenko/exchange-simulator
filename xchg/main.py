'''Simulator of a currency exchange.'''

import pandas as pd
from os import path
from os import listdir
from .common import _read_csv


def _read_market(data_path: str) -> pd.core.frame.DataFrame:
    '''Read all csv files with candles inside the directory and compose
    a Pandas DataFrame.

    Args:
        data_path: Where csv files with data are stored.

    Returns a Pandas DataFrame containing all candles for all
    currencies.
    '''
    market = None
    for idx, filename in enumerate(sorted(listdir(data_path))):
        df = _read_csv(path.join(data_path, filename))
        df['currency'] = path.splitext(filename)[0]
        market = pd.concat([market, df])
    return market


def next_step(data_path: str) -> dict:
    '''Go to the next step in timeline, it yelds a one new candle for each
       currency.

    Args:
       data_path: Where csv files with data are stored.

    Returns dictionary with currencies and their prices.
    '''
    market = _read_market(data_path)
    for step in market.index.unique():
        yield market.loc[step].set_index('currency').to_dict('index')
