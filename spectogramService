#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import signal
from skimage import util
import glob
datatest = (glob.glob("./wav/*.wav")) #czytanie plików z lokalizacji
# datatest #pokazuje liste plików
M=1024
rate = [None]*len(datatest)
audio = [None]*len(datatest)
freqs = [None]*len(datatest)
times = [None]*len(datatest)
Sx = [None]*len(datatest)
f = [None]*len(datatest)
ax = [None]*len(datatest)

for i in range(5):
    rate[i], audio[i] = wavfile.read(datatest[i])
    freqs[i], times[i], Sx[i] = signal.spectrogram(audio[i], fs=rate[i], window='hanning',
                                      nperseg=1024, noverlap=M - 100,
                                      detrend=False, scaling='spectrum')
    f[i], ax[i] = plt.subplots(figsize=(4.8, 2.4))
    ax[i].pcolormesh(times[i], freqs[i] / 1000, 10 * np.log10(Sx[i]), cmap='viridis')
    ax[i].axis('off')
    f[i].savefig('./obrazkitest/'+datatest[i][6:-4]+'.png', bbox_inches='tight', pad_inches=0)
    
# LABELSY Z CSV POSORTOWANE

from pandas import DataFrame
data = pd.read_csv("./data1/ff1010bird_metadata_2018.csv") 
df = DataFrame(data, columns = ['itemid','hasbird'])
df.sort_values(by=['itemid'], inplace=True)
test=df.loc[:,"hasbird"]
labels = list(test)
labels
