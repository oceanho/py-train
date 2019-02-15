"""
Python decorator manager
"""

import logging
import functools
from enum import Enum, unique

print(__name__)
from py001.log import Logger

permissions = [
    "admin.login",
    "admin.user.deletion",
    "admin.user.updation.name",
    "admin.user.updation.email",
    "admin.user.updation.disable",
    "admin.user.creation"
]

class PermissionDeniedExecption(Exception):
    pass

@unique
class PermMode(Enum):
    Strict=1
    Normal=2

class PermissionManager(object):
    """
    A Permission Manager object
    """
    def __init__(self, permissions):
        self.permissions = permissions

    def check(self, perm,mode=PermMode.Strict):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('Call %s %s():' % (perm, func.__name__))
                for p in self.permissions:
                    if p == perm:
                        return func(*args, **kw)
                if mode == PermMode.Strict:
                    raise PermissionDeniedExecption("Permission {perm} is not allowed.".format(perm=perm))
                Logger("PermissionManager.manager").logger.error("Permission {perm} is not allowed.".format(perm=perm))
            return wrapper
        return decorator
