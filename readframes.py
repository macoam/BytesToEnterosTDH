import wave
import numpy as np


goodmorning = wave.open('good-morningMan.wav', 'r')

frames = goodmorning.readframes(-1)

print(frames[:10])

ondaconvertida = np.frombuffer (frames, dtype='int16')

print (ondaconvertida[:10])