"""EE599 Activity 1 - Pitch and Spectrum Centroid Detection

Group:
    - Warnakulasuriya R.    E/17/371
    -                       E/17/372
    -
    -
    -
"""
import logging
import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram

## Set up logging
logging.basicConfig(format="[%(name)s][%(levelname)s] %(message)s")
logger = logging.getLogger("ee599-a1")
logger.setLevel(logging.DEBUG)

## Read wavefile
in_path = "C:\\Users\\User Files\\Documents\\University\\Misc\\4th Year Work\\EE599\\EE599 Activity 1"
in_file = "Senzawa Minecraft Stream Music.wav"
## Properties
bpm = 93
beatsperbar = 3
f_s, signal = wavfile.read(f"{in_path}//{in_file}")
window_size = round(f_s*60/bpm*beatsperbar)
bins = 
logger.debug(f"samples: {len(signal)}")
logger.debug(f"seconds: {len(signal)/f_s}")
logger.debug(f"beats:   {len(signal)/f_s/60*bpm}")
logger.debug(f"bars:    {len(signal)/f_s/60*bpm/beatsperbar}")
logger.debug(f"window:  {window_size} samples")


