from urllib.request import urlretrieve

online_prefix = 'https://raw.githubusercontent.com/jiafengkevinchen/CS-287-HW2/master/models/'

files = [
    'utils.py',
]

for fname in files:
    urlretrieve(online_prefix + fname, filename=fname)
