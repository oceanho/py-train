#!/usr/bin/env python3
#

from functools import reduce

def calc_product(x,y):
    return x * y

product = reduce(calc_product, [1, 2, 3, 4] )
print(product)
