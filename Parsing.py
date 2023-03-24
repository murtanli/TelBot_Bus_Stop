import random
from bs4 import BeautifulSoup as bs
import requests

class parser():
    def __init__(self,text):
        self.text = text

    def parsing_Web_site(self):
        headers = {
            "User-Agent": "Chrome/192.168.1.8"
        }
        URL_TEMPLATE = "https://ru.busti.me/kazan/stop/id/12315/"# name bus stop

        con = requests.get(URL_TEMPLATE, headers=headers).content
        soup = bs(con, "html.parser")
        parse = soup.find_all('tr')

        if len(parse) == 0:
            return "None"
        else:
            return parse


