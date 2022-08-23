#Fourier series in the real form of  a real-valued function of one real variable
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

#t is the independent value
P = 3 #period value
BT = -6 #initian value of t (begin time)
ET = 6 #final value of t (end time)
FS = 1000 #number of discrete values of t between BT and ET

#the periodic real-value funciton f(t) with period equal to P
f = lambda t: ((t % P) - (P/2.)) ** 3

#all discrete values of t in the interval from BT and ET
t_range = np.linspace(BT, ET, FS)
y_true = f(t_range) #the true f(t)

#function that computes the real fourier couples of coefficients (a0, def computer_real_fourier coeffs(func,N)):
def coeffs(func, N):
    result = []
    for n in range(N+1):
        an = (2./P) * spi.quad(lambda t: func(t) * np.cos(2 * np.pi * n * t / P), 0, P) [0]
        bn = (2./P) * spi.quad(lambda t: func(t) * np.sin(2 * np.pi * n * t / P), 0, P) [0]
        result.append((an,bn))
    return np.array(result)

#function that computes the real form Fourier series using an and bn
def func_coeffs(t, AB):
    result = 0,
    A = AB[:,0]
    B = AB[:,1]
    for n in range(0,len(AB)):
        if n > 0:
            result += A[n] * np.cos(2 * np.pi * n * t / P) + B[n] * np.sin(2. * np.pi * n * t / P)
        else:
            result += A[0]/2
    return result
maxN = 8
COLs = 2 #cols of plt
ROWs = 1 * (maxN-1) // COLs #rows of plt
plt.rcParams['font.size'] = 8
fig, axs = plt.subplots(ROWs, COLs)
fig.tight_layout(rect=[0,0,1,0.95],pad=3.0)
fig.suptitle('f(t) = ((t % P) - (P / 2.)) ** 3 where P= ' + str(P))

#plot, in the range from BT to ET, the true f(t) in blue and the approximation in red
for N in range(1, maxN + 1):
    AB = coeffs(f, N) #contains the list of couples of (an, bn) coefficients for n in 1...N interval.
    y_approx = func_coeffs(t_range,AB) #contains the discrete values of approximation outputted by the Fourier Series
    row = (N-1) // COLs
    col = (N-1) % COLs
    axs[row, col].set_title('case N=' + str(N))
    axs[row, col].scatter(t_range, y_true, color='green', s=1, marker = '.')
    axs[row, col].scatter(t_range, y_approx, color='red', s=2, marker = '.')
plt.show()
