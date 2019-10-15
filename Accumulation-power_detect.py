import wave
import struct
from scipy import fromstring, int16
import numpy as np
from pylab import *
%matplotlib inline

wavfile = 'test_moriao_100.wav'
wr = wave.open(wavfile, "rb")
ch = wr.getnchannels()
width = wr.getsampwidth()
fr = wr.getframerate()
fn = wr.getnframes()

N = 2560
span = 30

#N = 100
#span = 30

#N = 256
#span = 150

print('チャンネル', ch)
print('総フレーム数', fn)
print('サンプル時間', 1.0 * N * span / fr, '秒')

origin = wr.readframes(wr.getnframes())
data = origin[:N * span * ch * width]
wr.close()

print('現配列長', len(origin))
print('サンプル配列長: ', len(data))

X = np.frombuffer(data, dtype="int16")

def fourier (x, n, w):
    K = []
    for i in range(0, w-2):
        sample = x[i * n:( i + 1) * n]
        partial = np.fft.fft(sample)
        K.append(partial)

    return K

def inverse_fourier (k):
    ret = []
    for sample in k:
        inv = np.fft.ifft(sample)
        ret.extend(inv.real)

    print (len(sample))
    return ret

Kr = fourier(X, N, span)
freqlist = np.fft.fftfreq(N, d=1/fr)
amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in Kr[25]]
plot(freqlist, amp, marker= 'o', linestyle='-')
axis([0, 5000 , 0, 520000])

#amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in Kr[2500]]
plot(freqlist, amp, marker= 'o', linestyle='-')
