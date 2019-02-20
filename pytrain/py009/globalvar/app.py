#!/usr/bin/env python3
#

def set_global_var():
    global result
    result = "I'am a global variable."

# NameError: name 'result' is not defined
#print("result is {}",result)

set_global_var()
# working fine
print("result is",result)