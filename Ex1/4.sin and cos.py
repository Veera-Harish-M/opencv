'''Plot the value of sinx at an interval of every π/12 within a range of x as [0 : 2π]. 
In the same graph, plot cosx with same specification. 
Add legend to both the plots. 
Add x-label as x, y-label as ’function of x’ in the graph. 
Save the graph in .fig format.'''


import numpy as np
import matplotlib.pyplot as plot
import math

time        = np.arange(0, 2*math.pi, math.pi/12)
amplitude   = np.sin(time)
amplitude_1   = np.cos(time)

plot.xlabel('x')
plot.ylabel('function of x')

plot.plot(time, amplitude, "-o",color="blue", label="sine")
plot.stem(time,amplitude, linefmt='green' )
plot.plot(time, amplitude_1,"-o",color="red", label="cosine")
plot.legend(loc="lower left")
plot.stem(time,amplitude_1, linefmt='yellow' )

plot.savefig('sine_cos.jpg')
plot.show()
