import os

from IPython.paths import get_ipython_dir
from urllib.request import urlretrieve

startup_dir = os.path.join(get_ipython_dir(), 'profile_default', 'startup')
online_prefix = 'https://raw.githubusercontent.com/frtennis1/ipy-config/master/'

files = [
    'file-system-exporter.py',
]

for i, fname in enumerate(files):
    urlretrieve(online_prefix + fname,
        filename=os.path.join(startup_dir, '%03i-%s' % (i, fname)))
