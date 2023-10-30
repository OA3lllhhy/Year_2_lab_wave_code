Import numpy as np
Import matplotlib.pyplot as plt
from scipy import signal

x1, y1 = np.loadtxt('/Users/liuhaoyun/Desktop/Uni/Year_2/Year_2_Lab/Year_2_lab_waves/PART2_Thermal_Waves/data_sets/thermal_4min_a.txt', unpack = True, skiprows = 3)
x2, y2 = np.loadtxt('/Users/liuhaoyun/Desktop/Uni/Year_2/Year_2_Lab/Year_2_lab_waves/PART2_Thermal_Waves/data_sets/thermal_4min_b.txt', unpack = True, skiprows = 3)

def square(t):
    A = 50
    tau = 240
    return A*signal.square(2 * np.pi * t/tau)+50 

def T_n1(t):
    T_1 = 50 + (200 / np.pi) * np.sin(np.pi * t /120)
    return T_1

plt.figure(figsize=(12,8))
plt.plot(x1,y1,label=' Data a')
plt.plot(x2,y2,label=' Data b')
plt.plot(x1,T_n1(x1/10),label='Fundamental of square')
plt.plot(x1,square(x1/10),label='Ideal Sqaure')
plt.xlabel("Time ($10^{-1}s$)")
plt.ylabel("Temperature ($ \degree C$)")
plt.xlim(0,9600)
plt.legend()
plt.grid()
plt.show()

# Make a sine fit to x1,y1
def sine(t, A, f, phi):
    return A * np.sin(2 * np.pi * f * t + phi)

from scipy.optimize import curve_fit
popt, pcov = curve_fit(sine, x1, y1, p0=[100, 1/120, 0])
print(popt)
print(pcov)
plt.figure(figsize=(12,8))
plt.plot(x1,y1,label=' Data a')
plt.plot(x1,sine(x1,*popt),label='Sine fit')
plt.xlabel("Time ($10^{-1}s$)")
plt.ylabel("Temperature ($ \degree C$)")
plt.xlim(0,9600)
plt.legend()
plt.grid()
plt.show()

