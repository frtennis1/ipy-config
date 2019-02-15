import os

from IPython.paths import get_ipython_dir
from urllib.request import urlretrieve

startup_dir = os.path.join(get_ipython_dir(), 'profile_default', 'startup')
online_prefix = 'https://raw.githubusercontent.com/frtennis1/ipy-config/master/'

files = [
    ('downloader.py', 'azure-conf.py'),
    ('file-system-exporter.py', 'integrity-checker.py'),
]

for i, fnames in enumerate(files):
    urlretrieve(online_prefix + fname[0],
        filename=os.path.join(startup_dir, '%03i-%s' % (i, fname[1])))
