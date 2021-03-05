# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import re


def get_html(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        _html = ""
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            _html = resp.text
        return _html
    except Exception as e:
        print(e)
        return False

url = '' # Bank URL
old = []
now = []

while True:
    html = get_html(url)
 
    if html != False:
        soup = BeautifulSoup(html, 'html.parser')
        waiting = soup.find_all('td')
        old = now
        now = []
        for person in waiting:
            now.append(re.findall("\d+", person.text))
            
        if len(old) > 0 and len(now) > 0:
            for index, value in enumerate(now):
                try:
                    if value > old[index]:
                        if index == 0:
                            print("General counseling")
                            print("{} -> {} more people".format(old[index], value))
                        elif index == 1:
                            print("Loan counseling")
                            print("{} -> {} more people".format(old[index], value))
                        elif index == 2:
                            print("Corporate counseling")
                            print("{} -> {} more people".format(old[index], value))
                        elif index == 3:
                            print("VIP counseling")
                            print("{} -> {} more people".format(old[index], value))
                        else:
                            print("Unknown counseling")
                            print("{} -> {} more people".format(old[index], value))
                    elif value < old[index]:
                        if index == 0:
                            print("General counseling")
                            print("{} -> {} less people".format(old[index], value))
                        elif index == 1:
                            print("Loan counseling")
                            print("{} -> {} less people".format(old[index], value))
                        elif index == 2:
                            print("Corporate counseling")
                            print("{} -> {} less people".format(old[index], value))
                        elif index == 3:
                            print("VIP counseling")
                            print("{} -> {} less people".format(old[index], value))
                        else:
                            print("Unknown counseling")
                            print("{} -> {} less people".format(old[index], value))
                except Exception as e:
                    print(e)
    else:
        print('Skip')
    time.sleep(10)