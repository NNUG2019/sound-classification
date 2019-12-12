
# coding: utf-8
import glob
datatest = (glob.glob("./ptaszki/*.wav")) #czytanie plików z lokalizacji
# datatest #pokazuje liste plików

rate = [None]*len(datatest)
audio = [None]*len(datatest)
freqs = [None]*len(datatest)
times = [None]*len(datatest)
Sx = [None]*len(datatest)
f = [None]*len(datatest)
ax = [None]*len(datatest)

for i in range(0, len(datatest)):
    rate[i], audio[i] = wavfile.read(datatest[i])
    freqs[i], times[i], Sx[i] = signal.spectrogram(audio[i], fs=rate[i], window='hanning',
                                      nperseg=1024, noverlap=M - 100,
                                      detrend=False, scaling='spectrum')
    f[i], ax[i] = plt.subplots(figsize=(4.8, 2.4))
    ax[i].pcolormesh(times[i], freqs[i] / 1000, 10 * np.log10(Sx[i]), cmap='viridis')
    ax[i].set_ylabel('Frequency [kHz]')
    ax[i].set_xlabel('Time [s]');