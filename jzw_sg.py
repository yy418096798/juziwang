#!/usr/bin/env python
# coding: utf-8
# 句子网
# http://www.duanju.cc


import requests
from lxml import etree
import time


# 获取标题、文章地址
def get_href(one_url):
    r = requests.get(one_url)
    r.encoding = r.apparent_encoding
    tree = etree.HTML(r.text)
    title = tree.xpath("//div[@class='l-body']/div/ul/li/a/text()")
    href = tree.xpath("//div[@class='l-body']/div/ul/li/a/@href")
    hrefs = "http://www.duanju.cc" + href
    return title, hrefs

# 初始url拼接
def page_url(page):
    urls = "http://www.duanju.cc/shanggan/list_2_{}.html".format(page)
    return urls

# # 拼接地址
# def title_url(href):
#     hrefs = "http://www.duanju.cc" + href
#     return hrefs

# 数据下载
def infermation():
    list = []
    for page in range(1, 79):
        print(page_url(page))
        one_url = page_url(page)
        titles, hrefs = get_href(one_url)
        # print(len(titles), len(hrefs))
        for t, h in zip(titles, hrefs):
            # print(t,h)
        #     list.append({t:h})
        # print(list)
            with open(r"daly5-31/data.csv", "a") as f:
                f.write("".join(t)+",")
                f.write("".join(h)+"\n")
        # break



if __name__ == "__main__":
    infermation()