import pkgutil
import inspect
import json
from .help import Helper as H_Helper

__all__ = []
Helper = {}

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    if hasattr(module,'Helper'):
        Helper.update(getattr(module,'Helper'))
    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        if inspect.isfunction(value):
            globals()[name] = value
            __all__.append(name)

with open('../config/config.json', 'r') as json_file:
    data = json.load(json_file)
json_file.close()
data['Helper'] ={}
data['Helper'].update(Helper)
data['Commands'] = {'User_Cmd': [], 'Admin_Cmd': []}
for cmd in __all__:
    if '!'+cmd in Helper:
        if Helper['!'+cmd]['Type']=='Admin':
            data['Commands']['Admin_Cmd'].append('!'+cmd)
        else:
            data['Commands']['User_Cmd'].append('!'+cmd)

with open('../config/config.json', 'w') as json_file:
    json.dump(data, json_file, indent=2, sort_keys=True)
json_file.close()
