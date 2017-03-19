# -*_coding:utf8-*-
# Created by frank at 19/03/2017

import os
import glob
import shutil

"""
将所有的图片移动到images文件夹
"""
print(os.getcwd())
# os.mkdir('images')
print(glob.glob('*.jpg'))

# 方法一：shutil.move
# for image in glob.glob('*.jpg'):
#     shutil.move(image, './images')

# 方法二：os.rename
for image in glob.glob('*.jpg'):
    os.rename(image, './images/'+image)