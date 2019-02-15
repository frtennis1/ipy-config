from urllib.request import urlretrieve

online_prefix = 'https://raw.githubusercontent.com/frtennis1/ipy-config/master/'

files = [
    'file-system-exporter.py',
]

for fname in files:
    urlretrieve(online_prefix + fname, filename=fname)
