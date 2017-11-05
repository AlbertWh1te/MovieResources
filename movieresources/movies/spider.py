# -*- coding: utf-8 -*-
"""
movie spider
"""

import requests
from bs4 import BeautifulSoup
from movies.utils import base_url, headers, time_config


number_to_url = lambda number:base_url + time_config + str(number)+".html"

class MovieInfo(dict):
    """
    extend dict class to check if there is missing
    infomation
    """
    def hasNone(self):
        for value in self.values():
            if not value:
                return True
        return False

def url_to_raw(url):
    raw = None
    try:
        raw = requests.get(url,headers=headers)
    except Exception as e:
        print(e)
    return raw

def get_info(raw):
    if raw:
        info = MovieInfo()
        soup = BeautifulSoup((raw.content), "html.parser")
        info['name'] = get_name(soup)
        info['link'] = get_link(soup)
        return info
    return None

def get_name(soup):
    name = soup.find('h2')
    if name:
        return name.contents[0]
    return None

def get_link(soup):
    link = soup.find(target='_blank')
    if link:
        return link.get('href',None)
    return None

def number_to_info(number):
    return get_info(url_to_raw(number_to_url(number)))


if __name__ == '__main__':
    for i in range(100010,100020):
        print(number_to_info(i))
