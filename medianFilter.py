

def eval(x1,x2):
    xout = []
    for i in range(len(x1)):
        xout.append(x1[i] + x2[i])
        
    return xout
    
def median_filter(x):
    out = []
    for i in range(len(x)):
        if i == 0:  
            y = [0, x[0], x[1]]
        elif i == len(x) - 1: 
            y = [x[i-1], x[i], 0]
        else: 
            y = [x[i-1], x[i], x[i+1]]
            
        median = sorted(y)[1]
        
        out.append(median)
        
    return out
    
x1 = [0,1,0,0,0]
x2 = [0,0,100,0,0]

xsum = eval(x1,x2)

med_xsum = median_filter(xsum)
    
y1 = median_filter(x1)
y2 = median_filter(x2)

ysum = eval(y1,y2)

print("x1   =", x1)
print("x2   =", x2)
print("xsum =", xsum)
print("med_xsum =", med_xsum)
print("y1   =", y1)
print("y2   =", y2)
print("ysum =", ysum)


