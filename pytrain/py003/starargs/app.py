"""
Python argument of star
"""

import sys

def call_stack(func):
    def warpper(*args, **kw):
        print("Call function {0}()".format(func.__name__))
        return func(*args, **kw)
    return warpper

@call_stack
def star_1(a,*b):
    print(
        "Args length: {len}\n"
        "Args *b type {tb}, value is {vb}".format(len=sys.argv.__len__(),tb=type(b),vb=b))

@call_stack
def star_2(a,*b,**c):
    print(
        "Args length: {len}\n"
        "Args *b type {tb}, value is {vb}\n"
        "Args **c type {tc}, value is {vc}".format(len=len(sys.argv),tb=type(b),vb=b,tc=type(c),vc=c)
    )

star_1(1,2,3,4)
print("\n")
star_2(1,2,3,4,c1='c1',c2=b'0xFF')

