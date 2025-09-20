def echo_system(x, delay=4, alpha=0.5):
    y = []
    for n in range(len(x)):
        if n - delay >= 0:
            echo = x[n - delay] 
        else: 
            echo = 0
        y.append(x[n] + alpha * echo)
    return y
    
    
def eval(x1,x2):
    xout = []
    for i in range(len(x1)):
        xout.append(x1[i] + x2[i])
        
    return xout


x1 = [1, 0, 0, 0, 0, 0, 0]
x2 = [0, 0, 1, 0, 0, 0, 0]

xsum = eval(x1,x2)

xsumEcho = echo_system(xsum)

y1 = echo_system(x1)
y2 = echo_system(x2)

ysum = eval(y1,y2)

print("x1 = ", x1)
print("x2 = ", x2)
print("xsum =", xsum)
print("xsumEcho =", xsumEcho)
print("y1 = ", y1)
print("y2 = ", y2)
print("ysum =", ysum)

print(f"\nIs Function Linear:")
print("Yes" if ysum == xsumEcho else "No")
