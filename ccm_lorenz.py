import numpy as np
import skccm
import seaborn as sns
sns.set_style('ticks')
sns.set_context(context='paper',font_scale=1.5)
from sklearn.model_selection import train_test_split
from simulate_dynamics import DataGenerator
import matplotlib.pyplot as plt

def ccm_causality(tseries1, tseries2):
    #Prepare Data(Embedding)
    lag = 18
    edim = 3
    e1 = skccm.Embed(tseries1)
    e2 = skccm.Embed(tseries2)
    x1 = e1.embed_vectors_1d(lag,edim)
    x2 = e2.embed_vectors_1d(lag,edim)
    #Split
    x1tr,x1te,x2tr,x2te = train_test_split(x1,x2,test_size = .25)
    #Fit
    CCM = skccm.CCM()
    CCM.fit(x1tr,x2tr)
    #Set Library Lengths(Why do we need this?)
    len_tr = len(x1te)
    lib_lens = np.arange(10, len_tr, len_tr/20, dtype='int')
    #Predict
    x1p, x2p = CCM.predict(x1te,x2te,lib_lengths = lib_lens)
    #Score
    sc1, sc2 = CCM.score()

    plt.plot(lib_lens, sc1, label='Forecast Skill for x1')
    plt.plot(lib_lens, sc2, label='Forecast Skill for x2')
    plt.xlabel('Library Length')
    plt.ylabel('Forecast Skill')
    plt.title('Forecast Skill vs Library Length')
    plt.legend()
    plt.grid(True)
    plt.show()
    

if __name__ == "__main__":
    #Get Lorenz Data
    lorenz_generator = DataGenerator(DataGenerator.lorenz96)
    L_Data = lorenz_generator.simulate(6,10000) #Why does 3 returns a straight line?
    X = L_Data[0]
    ccm_causality(X[:,0],X[:,1])
