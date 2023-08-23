"""EE599 Activity 1 - Pitch and Spectrum Centroid Detection

Group:
    - Warnakulasuriya R     E/17/371
    - Warnasooriya WAVG     E/17/372
    -
    -
    -
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
window_size = f_s*0.25
window_gap = f_s*0.05
window_count = math.ceil(len(yy)/window_size)
logger.debug(f"sample rate:     {f_s} Hz")
logger.debug(f"samples:         {len(yy)}")
logger.debug(f"duration:        {len(yy)/f_s} s")
logger.debug(f"window size:     {window_size/f_s*1000:.0f} ms")
logger.debug(f"window overlap:  {window_gap/window_size*100:.0f} %")
## Analysis
y_trimmed = yy[:f_s]
aa = librosa.lpc(y_trimmed, order=128) # coefficients of lpc function
xx = np.zeros_like(y_trimmed)
xx[0] = 1
y_hat = signal.lfilter(np.array([1]),aa,xx)
f_poles = f_s*np.sort(np.angle(np.roots(aa)))/(2*np.pi)
f_poles_abs = np.sort(np.abs(f_poles))
f_poles_abs = f_poles_abs[f_poles_abs != 0]
logger.info(f"fundamental: {f_poles_abs[1]} Hz")

