# -*_coding:utf8-*-
# Created by frank at 19/03/2017
import re
import requests
from utils import get_header
with open("all_page_html.txt", 'r') as f:
    html = f.read()
    links = re.findall('<a href="(.*?)" rel="', html)
    # print(links)
    print("%d images total before remove duplicates" % len(links))

    remove_dump_links = list(set(links))
    print("%d images total after remove duplicates" % len(remove_dump_links))

print(links)

# 尝试下载一张图片
i = 1
for link in remove_dump_links:
    image = requests.get(link, headers=get_header())
    # print(image.content)
    with open(str(i)+'.jpg', 'wb') as p:
        p.write(image.content)
    print('下载得到图片！保存图片' + str(i) + '大小为' + str(len(image.content)))
    i += 1
print("done")