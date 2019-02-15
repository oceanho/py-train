"""
Entry point
"""

import sys
import importlib

if len(sys.argv) < 2:
    print("missing arguments")
    sys.exit(127)    

app_name = sys.argv[1]
app_maps=[
    { "app":"001", "path":"py001.app"},
    { "app":"002", "path":"py002.contextmanager.app"},
    { "app":"003", "path":"py003.starargs.app"},
    { "app":"004", "path":"py004.decorator.app"},
]

for app in app_maps:
    if app['app'] == app_name:
        importlib.import_module(app['path'])
