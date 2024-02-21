import pandas as pd# Your list of items

"""
Input a list of Polygon Aggregates
Outputs a DataFrame with the json items parse into columns
"""
def polygon_to_df(items):
    data = []
    for item in items:
        data.append({
            "open": item.open,
            "high": item.high,
            "low": item.low,
            "close": item.close,
            "volume": item.volume,
            "vwap": item.vwap,
            "timestamp": item.timestamp,
            "transactions": item.transactions,
            "otc": item.otc
        })# Creating a DataFrame
    df = pd.DataFrame(data)

def 