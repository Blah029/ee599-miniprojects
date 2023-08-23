"""EE599 Activity 1 - Pitch and Spectrum Centroid Detection

Group:
    - Warnakulasuriya R     E/17/371
    - Warnasooriya WAVG     E/17/372
    -
    -
    -

References:
    - https://numpy.org/doc/stable/reference/generated/numpy.pad.html
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html
"""
import logging
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import io
from scipy import signal

## Set up logging
logging.basicConfig(format="[%(name)s][%(levelname)s] %(message)s")
logger = logging.getLogger("ee599-a1")
logger.setLevel(logging.DEBUG)

## Read wavefile
in_path = "C:\\Users\\User Files\\Documents\\University\\Misc\\4th Year Work\\EE599\\EE599 Activity 1\\Samples"
# in_path = "data"
in_file = "Senzawa Minecraft Stream Music.wav"
# in_file = "sarigamapa.wav"
f_s, data = io.wavfile.read(f"{in_path}\\{in_file}")
## Properties
bpm = 93
beatsperbar = 3
window_size = round(f_s*60/bpm*beatsperbar)
window_count = math.ceil(len(data)/window_size)
logger.debug(f"input shape: {data.shape}")
logger.debug(f"sample rate: {f_s} Hz")
logger.debug(f"samples:     {len(data)}")
logger.debug(f"duration:    {len(data)/f_s} s")
logger.debug(f"beats:       {len(data)/f_s/60*bpm}")
logger.debug(f"bars:        {len(data)/f_s/60*bpm/beatsperbar}")
logger.debug(f"window size: {window_size} samples")
logger.debug(f"windows:     {window_count}")
## Analysis
bins = np.array([[0,20],[20,200],[200,2000],[2000,20000]]) ## replace with notes
psd = np.zeros((window_count,len(bins)))
for i in range(window_count):
# for i in range(1):
    start = i*window_size
    end = (i+1)*window_size
    ## Pad last window if necessary
    if end > len(data):
        data_window = np.pad(data[start:],((0,end-len(data)),(0,0)),"constant")
        logger.debug(f"window number {i} padded: \n{data_window}")
        logger.debug(f"padded shape: {data_window.shape}")
    else:
        data_window = data[start:end]
    ff,tt,sff = signal.spectrogram(data_window,f_s)
    logger.debug(f"frequency shape: {ff.shape}, time shape: {tt.shape}, spectrogram shape: {sff.shape}")
    ## Calculate power of bins
    for j,bin in enumerate(bins):
        bin_ff = ff[(ff >= bin[0]) & (ff < bin[1])]
        bin_indices = [np.where(ff == binnedf)[0][0] for binnedf in bin_ff]
        avgpower = np.mean(sff[bin_indices], axis=0)
        psd[i,j] = np.mean(avgpower)
        # logger.debug(f"j: {j}, bin: {bin}, binned len: {len(bin_ff)}")
        logger.debug(f"indices shape: {np.array(bin_indices).shape}, sff shape: {sff.shape}")
        # logger.debug(f"avg shape: {avgpower}")
## Plot
x_temp = np.arange(0,20,20/len(psd)) ## 1st bin
fig,ax = plt.subplots(1)
ax.set_xscale("log")
ax.plot(x_temp,psd[:,0])
plt.show()
