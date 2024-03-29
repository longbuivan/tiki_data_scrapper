from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

all_list = []

def menu_extract(link):

    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')

    menu_list = bs.find_all("a", attrs={"class":re.compile('MenuItem_')})

    for menu in menu_list:
        all_list.append(menu['href'])
        # print(menu_list)
    return all_list

# print(menu_extract)

