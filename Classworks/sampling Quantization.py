# ploting sin wave and sampling it and quantizing it 

import numpy as np
import matplotlib.pyplot as plot
import math

figure, axis = plot.subplots(2, 3)
time        = np.arange(0, 2*math.pi, math.pi/12)
amplitude   = np.sin(time)
amplitude_1   = np.cos(time)

plot.xlabel('x')
plot.ylabel('function of x')


axis[0, 0].plot(time, amplitude)
axis[0, 0].set_title("Sine wave")

axis[0, 1].plot(time, amplitude)
axis[0, 1].set_title("Sampling")
axis[0, 1].stem(time,amplitude, 'r', )

axis[0, 2].plot(time, amplitude, 'o', color='black')
axis[0, 2].set_title("Quantization")
axis[0, 2].stem(time,amplitude, 'r', )


axis[1, 0].plot(time, amplitude_1)
axis[1, 0].set_title("Cos wave")

axis[1, 1].plot(time, amplitude_1)
axis[1, 1].set_title("Sampling")
axis[1, 1].stem(time,amplitude_1, 'r', )

axis[1, 2].plot(time, amplitude_1, 'o', color='black')
axis[1, 2].set_title("Quantization")
axis[1, 2].stem(time,amplitude_1, 'r', )


plot.show()

