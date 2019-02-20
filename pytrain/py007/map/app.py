
import math

def pow_2of2(num):
    return pow(num,2)

def pow_2of3(num):
    return pow(num,3)

def pow_2of4(num):
    return pow(num,4)

funcs = [pow_2of2,pow_2of3,pow_2of4]

for num in range(1,10):
    print(list(map(lambda f:f(num), funcs)))
