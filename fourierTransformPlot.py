# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 18:36:38 2015

@author: yifanli
"""
# import the usual libraries
import numpy as np
import matplotlib.pyplot as plt
# import the fourier transform functionality
from scipy.fftpack import fft,fftfreq #引入了 fast fourier transform 和 fftfreq 两个 function from scipy.fftpack 中。

data = np.loadtxt('squareWave.csv', delimiter=',', comments='#',skiprows=1) ##skiprows=1用来略去元数据中第一行的单词项。
data2 = np.loadtxt('squareWave_1.csv', delimiter=',', comments='#',skiprows=1)
data3 = np.loadtxt('squareWave_2.csv', delimiter=',', comments='#',skiprows=1)

##np.是用来从lbrary 中 选取所需的函数时用的。

# access the data columns and assign variables x,y,y_sigma. If you don't have error data, set "y_sigma = None"
time = data[:,0] ####y从源数据的第一列中选取。
y = data[:,1]
#y_sigma = 0.5

y2 = data2[:,1]
#y2_sigma = 0.5

y3 = data3[:,1]
#y2_sigma = 0.5
# plot wave as funtion of time
plt.plot(time,y)
plt.plot(time,y2)
plt.plot(time,y3)
plt.legend(['y','y2','y3'])

plt.xlim(0.0,5.0)
plt.ylim(-2.0,2.0)

plt.xlabel("Time t [s]")
plt.ylabel("Wave")

plt.title("Wave Signal")
plt.show()

# calculate the fourier transform -- spectral amplitude over frequencies
n = time.shape[-1]
transform=(fft(y)[:n/2]) * 2./n
transform2=(fft(y2)[:n/2]) * 2./n
transform3=(fft(y3)[:n/2]) * 2./n

#transform = np.zeros(149)
frequency = fftfreq(n,time[1]-time[0])[:n/2]

#for i in range(149):
 #  if frequency[i]<= 10:
 #      transform[i] = fft(y)[i]*2./14.9
 #  else: transform[i] = 0
## n is the amount of time data points
## transform is the normalized fourier transform in the positive frequency range - [:n/2]
## frequency is the positive frequency range based on the given time data

# plot the fourier transform
plt.plot(frequency,np.abs(transform))
plt.plot(frequency,np.abs(transform2))
plt.plot(frequency,np.abs(transform3))
plt.legend(['transform','transform2','transform3'])

plt.xlabel("Frequency f [Hz]")
plt.ylabel("Amplitude")
plt.title("Fourier Transform")
