import numpy as np  # mathematical library
import cmath        # another mathematical library
import matplotlib.pyplot as plt   # plotting mathematical library
from scipy import signal          # scientific calculation library

def transform(x):    # this is a fuction describe type in python
	y=[]
	for r in range(1000):   # this is basic range for function graphic
		m=complex(0)
		for t in range(len(x)):
			m+=x[t]*np.exp(-2*np.pi*1j*t*r/len(x))  # Fourier transform formula described as
		y.append(m)                                 # multiply to magnitudes between the space  
	return y

t=np.linspace(0,1,1000)            #sampled at 1000 Hz
f=np.cos(2*np.pi*5*t)+5*np.cos(2*np.pi*10*t)+np.cos(2*np.pi*15*t)+9*np.cos(2*np.pi*20*t) 
p=transform(f)                     # A complicate sound wave formula is up line
p=[j for j in p if 500>j>0]         # no negative frequencies and limiting the results
fig,(ax1,ax2)=plt.subplots(1,2)    # divide the plot zone two same piece

ax1.plot(f,color='green')          # Axes and inputs defined
ax1.set(xlabel='Time', ylabel='Magnitude') 
ax1.title.set_text('Sound Signal')
ax1.grid()
ax2.plot(p,color='magenta')#output
ax2.set(xlabel='frequency')
ax2.set_label('Fourier Transform')
ax2.title.set_text('Fourier Transform')   # they are all visual specials of graphic
ax2.grid()
plt.show()
