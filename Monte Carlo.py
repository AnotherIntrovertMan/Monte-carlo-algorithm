import numpy as np

#f(x) = x, f(x) selang [1,3]

n = 100 #banyak tebakan
a = 1
b = 3
f_min = 0
f_max = 3

def f(x): #f(x)=x
    return x

i =  0
Q = 0

while (i < n):
    Xi = np.random.uniform(a,b)
    Yi = np.random.uniform(f_min,f_max)
    func = f(Xi)
    if (Yi<=func):
        Q+=1
    i+=1

print(Q)
print("Aproksimasi integral: ", Q/n*(f_max-f_min)*(b-a))
