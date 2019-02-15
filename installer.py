import os
import subprocess

from IPython.paths import get_ipython_dir
from urllib.request import urlretrieve

startup_dir = os.path.join(get_ipython_dir(), 'profile_default', 'startup')

if not os.path.isdir(startup_dir):
    subprocess.run(['ipython', 'profile', 'create'])

downloader_url = 'https://raw.githubusercontent.com/frtennis1/ipy-config/master/downloader.py'

urlretrieve(downloader_url, filename=os.path.join(startup_dir, '000-azure-conf.py'))
