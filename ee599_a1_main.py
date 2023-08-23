"""EE599 Activity 1 - Pitch and Spectrum Centroid Detection

Group:
    - Warnakulasuriya R     E/17/371
    - Warnasooriya WAVG     E/17/372
    -
    -
    -

References:
    - https://librosa.org/doc/main/generated/librosa.lpc.html
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html
"""
import librosa
import logging
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

## Set up logging
logging.basicConfig(format="[%(name)s][%(levelname)s] %(message)s")
logger = logging.getLogger("ee599-a1")
logger.setLevel(logging.DEBUG)

## Read wavefile
# in_path = "C:\\Users\\User Files\\Documents\\University\\Misc\\4th Year Work\\EE599\\EE599 Activity 1\\Samples"
# in_file = "Senzawa Minecraft Stream Music.wav"
in_path = "data"
in_file = "sarigamapa.wav"
yy, f_s = librosa.load(f"{in_path}\\{in_file}")
## Properties
window_size = int(f_s*0.1)
window_gap = int(window_size*0.25)
window_count = math.floor((len(yy)-window_size)/window_gap) + 1
pole_count = 16
logger.debug(f"sample rate:     {f_s} Hz")
logger.debug(f"samples:         {len(yy)}")
logger.debug(f"duration:        {len(yy)/f_s} s")
logger.debug(f"window size:     {window_size} ({window_size/f_s*1000:.0f} ms)")
logger.debug(f"window gap:      {window_gap}")
logger.debug(f"window overlap:  {window_size - window_gap} ({window_gap/window_size*100:.0f} %)")
logger.debug(f"winodw count:    {window_count}")
## Analyse
pitch = []
y_hat = np.zeros_like(yy) 
for i in range(window_count):
    y_trimmed = yy[i*window_gap:i*window_gap + window_size]
    aa = librosa.lpc(y_trimmed, order=pole_count) # coefficients of lpc function
    xx = np.zeros_like(y_trimmed)
    xx[0] = 1
    y_hat_trimmed = signal.lfilter(np.array([1]),aa,xx)
    y_hat[i*window_gap:i*window_gap + window_size] = y_hat_trimmed
    f_poles = f_s*np.sort(np.abs(np.angle(np.roots(aa))))/(2*np.pi)
    for f_p in f_poles:
        if f_p != 0:
            pitch.append(f_p)
            break
    ## Plot
    if i == 0:
        logger.info(f"starting fundamental: {f_poles[1]:.2f} Hz")
        fig,ax = plt.subplots(2,2, num="Characteristics of 1st Window")
        fig.tight_layout()
        ax[0,0].title.set_text("LPC Coefficients")
        ax[0,0].bar(np.linspace(1,len(aa),len(aa)),aa,1)
        ax[0,1].title.set_text("Input Impulse")
        ax[0,1].stem(xx)
        ax[1,0].title.set_text("Synthesised Signal")
        ax[1,0].plot(y_hat_trimmed)
        ax[1,1].title.set_text("Frequencies of Poles (Magnitude)")
        ax[1,1].stem(f_poles)
fig,ax = plt.subplots(3, num="Final Observations")
fig.tight_layout()
ax[0].title.set_text("Input Signal")
ax[0].plot(yy)
ax[1].title.set_text("Synthesised Signal")
ax[1].plot(y_hat)
ax[2].title.set_text("Variation of Pitch")
ax[2].plot(pitch)
plt.show()


