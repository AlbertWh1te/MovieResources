# -*- coding: utf-8 -*-
"""
movie spider
"""

import requests
from bs4 import BeautifulSoup

from .utils import base_url,headers,time_config


number_to_url = lambda number:base_url + time_config + str(number)+".html"


def url_to_raw(url):
    raw = None
    try:
        raw = requests.get(url,header=headers)
    except Exception as e:
        print(e)
    return raw

def g 