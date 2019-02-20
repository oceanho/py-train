#!/usr/bin/env python3
#

import sys

condition=True
if len(sys.argv) > 1:
     condition = False
chooies = "Yes" if condition else "No"

print(chooies)

result = ("Args length > 1", "Args length <= 1")[condition]
print("Result is {}".format(result))