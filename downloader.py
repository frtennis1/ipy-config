import os
import pandas as pd

from IPython.paths import get_ipython_dir
from urllib.request import urlretrieve

startup_dir = os.path.join(get_ipython_dir(), 'profile_default', 'startup')
online_prefix = 'https://raw.githubusercontent.com/frtennis1/ipy-config/master/'

file_list = pd.read_csv(online_prefix + 'file-list.csv')

for i, fnames in file_list.iterrows():
    urlretrieve(online_prefix + fnames.online_name,
        filename=os.path.join(startup_dir, '%03i-%s' % (i+1, fnames.local_name)))
