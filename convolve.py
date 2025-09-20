import numpy as np

def convolve1s(x, h):
    Lx = len(x)
    Lh = len(h)
    Ly = Lx + Lh - 1   
    # length of h[-k]: len(X) + len(h) -1
    
    y = np.zeros(Ly)

    for n in range(Ly):
        for k in range(Lx):
            h_index = n - k
            
            if h_index >= 0 and h_index < Lh:
                product = x[k] * h[h_index]
                y[n] += product
                
    return y


x = np.array([1,2,3,4,5])    
h = np.array([6,7,8,9])     

y = convolve1s(x, h)

print("x =", x)
print("h =", h)
print("y =", y)
