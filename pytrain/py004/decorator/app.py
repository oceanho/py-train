"""
A easy decorator implement of permission system checker
"""

from manager import PermissionManager, PermMode, permissions as pms

pm = PermissionManager(pms)

@pm.check("admin.login")
def admin_login():
    pass

# Bad permission case
@pm.check("admin.login.001", PermMode.Normal)
def admin_login001():
    pass

@pm.check("admin.user.creation")
def admin_user_creation():
    pass

#if __name__ == "__main__":
# Pass
admin_login()

# Perimission deined
admin_login001()

# Pass
admin_user_creation()