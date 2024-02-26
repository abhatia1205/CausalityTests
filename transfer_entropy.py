import numpy as np
import pyinform as pyi
import pandas as pd
import datetime as dt
from polygon import RESTClient
# from polygon import RESTClient
# client = RESTClient(api_key="qAECEY64BgfArsBJID6VYCJ1k0asFEll", trace=False)
# ticker = "AAPL"

'''
def get_stock_data_to_df(ticker):
    aggs = []
    B = client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000)
    # for a in B:
    #     aggs.append(a)
    # items = aggs
    data = []
    for item in B:
        # print(dir(item))
        data.append({
            "open": item.open,
            "high": item.high,
            "low": item.low,
            "close": item.close,
            "volume": item.volume,
            "vwap": item.vwap,
            "timestamp": item.timestamp,
            "transactions": item.transactions,
        
        })
    return pd.DataFrame(data)

def stationaryize(df : pd.DataFrame, time) -> pd.DataFrame:
    df['stationary'] = (np.log(df[time])).diff()
    df['timestamp_processed'] =  pd.to_datetime(df['timestamp'], unit='ms')
    df = df.dropna(how = 'any', axis = 0, )
    return df

def get_clean_data(ticker, open_or_close) -> pd.DataFrame:
    return stationaryize(get_stock_data_to_df(ticker.upper()), open_or_close)




client = RESTClient(api_key="qAECEY64BgfArsBJID6VYCJ1k0asFEll", trace=False)
ticker = "AAPL"
aapl_df = get_clean_data("aapl", 'close')
print(aapl_df.head())
'''





'''
xs = [0,1,1,1,1,0,0,0,0]
ys = [0,0,1,1,1,1,0,0,0]
print(pyi.transfer_entropy(xs, ys, k=2))
print(pyi.transfer_entropy(ys, xs, k=2))
'''

# pyinform.transferentropy.transfer_entropy(source, target, k, condition=None, local=False)