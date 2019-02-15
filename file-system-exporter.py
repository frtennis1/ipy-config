import os
import pwd
import getpass

user = getpass.getuser()

top_dirs = ['Documents', 'Desktop', 'Downloads']

all_files = []
for top_level in top_dirs:
    for root, dirs, files in os.walk(os.path.join('/', 'Users', user, top_level), topdown=False):
        for name in files:
            all_files.append(os.path.join(root, name))

with open('all-files.txt', 'w') as f:
    f.write('\n'.join(all_files))
