import requests
from bs4 import BeautifulSoup
import string
import re
import socket
import time
import socks
import json
num = list(range(1,100))
oid = str(input('输入av号(仅数字): '))
url = ['http://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&sort=0&' + 'oid=' + oid + '&pn={}'.format(str(i)) for i in num]
s = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
list1 =[]
key_word = input('输入要搜索的关键词: ')
# 打印出第一个热门评论及其作者:
#print(dict1['data']['hots'][0]['content']['message'] + '__________Author: ' + dict1['data']['hots'][2]['member']['uname'])
def get_all(self):
    wb_data = s.get(self, headers=headers)
    dict1 = wb_data.json()
    if dict1['data']['replies'] != []:
        for i in dict1['data']['replies']:
            if i['replies'] != []:
                for one in i['replies']:
                    # print(one['member']['uname'] + ' : ' + one['content']['message'])
                    list1.append(str(i['content']['message'] + '  -- 来自用户: ' + i['member']['uname'] + '  性别：' + i['member']['sex'] + '    ' + '----楼中楼: ' + one['member']['uname'] + ' : ' + one['content']['message']))
            else:
                list1.append(str(i['content']['message'] + '  -- 来自用户: ' + i['member']['uname'] + '  性别：' + i['member']['sex']))
        return list1
    else:
        raise ValueError
#搜索关键词
def search():
    try:
        for i in url:
            get_all(i)
    except ValueError:
        pass
    for a in list1:
        if key_word in a:
            print('\n' + 'Result: ')
            print(a)
        else:
            pass
search()
