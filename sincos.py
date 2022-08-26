import numpy as np
import matplotlib.pylab as plt
import math as m

pi = round(m.pi, 3)

x = np.arange(-2*m.pi, 2*m.pi, pi)
A = 1.
C = 2*pi
B = 0.0
D = 0.0

def sin(A,B,C,D):
    y = A*(np.sin((2*pi(x-B))/C))+D

    plt.plot(x,y)
    plt.axhline(y=0, color = 'k')
    plt.axvline(x=0, color = 'k')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    plt.show()
    return

def cos(A,B,C,D):
    y = A*(np.cos((2*pi(x-B))/C))+D

    plt.plot(x,y) #plot the graph of y function of x
    plt.axhline(y=0, color = 'k')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('cos(x)')

    plt.show()
    return

print("\n\t\t Sine and Cosine Trig graph calculator")
print("\t","-"*55)

end_program = 1

while end_program:
    c=int(input("Press 1 for sine or 0 for cosine: "))
    if c==1:
        print("You chose to grpah the function sine, the form:")
        print("Enter the graph properties when prompted:")
        A = float(input("Amplitude (A) = "))
        B = float(input("Phase shift (B) ="))
        C = float(input("Period (can't be 0)(C)= "))
        D = float(input("Vertical shift (D)= "))
        sin(A,B,C,D)
        end_program = int(input("Do you want another graph? Press 1 for Yes and 0 for No \n"))
    elif c==0:
        print("You chose to graph the function cosine, the form:")
        print("Enter the graph properties when prompted:")
        A = float(input("Amplitude (A) = "))
        B = float(input("Phase shift (B) ="))
        C = float(input("Period (can't be 0)(C)= "))
        D = float(input("Vertical shift (D)= "))
        cos(A,B,C,D)
        end_program = int(input("Do you want another graph? Press 1 for Yes and 0 for No \n"))
    else:
        print("Wrong choice, please try again")
        continue