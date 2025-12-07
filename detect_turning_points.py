import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    n = len(signal)
    turning_points = []
    
    for i in range(1, n - 1):
        if (signal[i] > signal[i - 1] and signal[i] > signal[i + 1]) or \
           (signal[i] < signal[i - 1] and signal[i] < signal[i + 1]):
            turning_points.append(i)
    
    turning_points = np.array(turning_points)

    plt.plot(signal, label='Signal') 
    plt.scatter(turning_points, signal[turning_points], color='red', label='Turning points')
    plt.legend()
    plt.savefig(filename)
    
    return turning_points
