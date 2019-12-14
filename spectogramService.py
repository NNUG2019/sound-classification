#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import signal
from skimage import util
import gc
import glob
datatest = (glob.glob("./ptaki/train/wav/*.wav")) #czytanie plików z lokalizacji
# datatest #pokazuje liste plików
M=1024
rate  = [None]*len(datatest)
audio = [None]*len(datatest)
freqs = [None]*len(datatest)
times = [None]*len(datatest)
Sx    = [None]*len(datatest)

for i in range(len(datatest)):
    rate[i], audio[i] = wavfile.read(datatest[i])
    freqs[i], times[i], Sx[i] = signal.spectrogram(audio[i], fs=rate[i], window='hanning',
                                      nperseg=1024, noverlap=M - 100,
                                      detrend=False, scaling='spectrum')
    f, ax = plt.subplots(figsize=(4.8, 2.4))
    ax.pcolormesh(times[i], freqs[i] / 1000, 10 * np.log10(Sx[i]), cmap='viridis')
    ax.axis('off')
    f.savefig('./imageptaki/train/'+datatest[i][18:-4]+'.png', bbox_inches='tight', pad_inches=0)
    plt.close('all')
    plt.clf()
    gc.collect()