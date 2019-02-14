"""
Demo of the context manager entry point
"""

import os
from manager import File

work_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    with File(os.path.join(work_dir,"files","test.txt")) as f:
        print("data is: {data}".format(data=f.read()))

