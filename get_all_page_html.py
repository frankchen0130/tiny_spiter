# -*_coding:utf8-*-
# Created by frank at 19/03/2017
import requests
import re

from utils import get_header

url_0 = "http://tw.gigacircle.com/3638546-1"


html = requests.get(url_0)

with open("iniUrl.txt", mode='w') as t:
    t.write(html.text)

# 从html.txt里面提取所有的地址

html_txt = open("iniUrl.txt", 'r').read()

# 提取到的url_0里面的所有链接
wanted_url = re.findall('<a href="(.*?)" rel="nofollow"', html_txt)

# 在对wanted_url里面每一个链接，再提取其中的链接
# 把这些链接html都写进一个文本文件

with open("all_page_html.txt", 'a+') as f:
    for link in wanted_url:
        _ = requests.get(link, headers=get_header())
        f.write(_.text)
    print("Done")



