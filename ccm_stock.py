from skccm.utilities import train_test_split
import skccm as ccm
from simulate_dynamics import DataGenerator
import yfinance as yf
import pandas as pd
import numpy as np
from skccm import Embed
import matplotlib.pyplot as plt

tickers = ['AAPL', 'META', 'XOM', 'LMT']
data = yf.download(tickers, start='2010-01-01', end='2024-01-01', progress=False)
adj_close = data['Adj Close']


#Stationarize data
stationary_df = np.log(adj_close) - np.log(adj_close.shift(1))
stationary_df = stationary_df.dropna()

#Stationary 1d arrays
AAPL_1d = stationary_df['AAPL']
META_1d = stationary_df['META']
XOM_1d = stationary_df['XOM']
LMT_1d = stationary_df['LMT']

print(AAPL_1d)
print(META_1d)


def trim_matrices(mat1, mat2):
    min_length = min(mat1.shape[0], mat2.shape[0])
    trimmed_mat1 = mat1[:min_length, :]
    trimmed_mat2 = mat2[:min_length, :]
    return trimmed_mat1, trimmed_mat2

#Calculating Lag
def get_lag(list):
    e = Embed(list)
    mutual_info = e.mutual_information(max_lag=100)  
    lag = np.argmin(mutual_info) + 1 
    return lag 

#Calculating Embedding
def get_embedding(list, embed_dim_param):
    e = Embed(list)
    X = e.embed_vectors_1d(get_lag(list), embed_dim_param)
    return X

def plot_forecast_skill_vs_library_length(x1_embedded, x2_embedded):
    x1tr, x1te, x2tr, x2te = train_test_split(x1_embedded, x2_embedded, percent=0.75)

    CCM = ccm.CCM()  # Initialize the CCM class

    #library lengths to test
    len_tr = len(x1tr)
    lib_lens = np.arange(10, len_tr, len_tr/20, dtype='int')

    #test causation
    CCM.fit(x1tr,x2tr)
    x1p, x2p = CCM.predict(x1te, x2te,lib_lengths=lib_lens)

    sc1,sc2 = CCM.score()

    plt.plot(lib_lens, sc1, label='Forecast Skill for x1')
    plt.plot(lib_lens, sc2, label='Forecast Skill for x2')
    plt.xlabel('Library Length')
    plt.ylabel('Forecast Skill')
    plt.title('Forecast Skill vs Library Length')
    plt.legend()
    plt.grid(True)
    plt.show()



#Testing
lag_AAPL = get_lag(AAPL_1d)
lag_META = get_lag(META_1d)

for i in range(2,26):
    AAPL_embed = get_embedding(AAPL_1d, i)
    META_embed = get_embedding(META_1d, i)
    trimmed_AAPL_embed, trimmed_META_embed = trim_matrices(AAPL_embed, META_embed)
    plot_forecast_skill_vs_library_length(trimmed_META_embed, trimmed_AAPL_embed)