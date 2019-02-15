"""
Python Class context manager demo
"""

class File(object):
    def __init__(self,path,mode='r+t'):
        self.file = open(path,mode=mode)
    def __enter__(self):
        return self.file
    def __exit__(self, type, value, traceback):
        self.file.close()