# -*- coding: utf-8 -*-
# import getAlla
from urllib import request
import pypandoc
import docx
from bs4 import BeautifulSoup #导入模块

from getdoc import MYHTMLParser
from tttchengym.geturl import HTMLClient

urllist = [
    "https://docs.ucloud.cn/security/uads/index",
    "https://docs.ucloud.cn/security/uewaf",
    "https://docs.ucloud.cn/security/uhas/index",
    "https://docs.ucloud.cn/security/udas",
    "https://docs.ucloud.cn/security/uws_robot"
    # "https://docs.ucloud.cn/security/uads/concepts/overview"
]
# url = "https://docs.ucloud.cn/security/uads/index" #网页地址
for url in urllist:

    wp = request.urlopen(url) #打开连接
    content = wp.read() #获取页面内容

    fp = open("testforurl.html","a+b") #打开一个文本文件
    fp.write(content) #写入数据
    fp.close() #关闭文件

# def htmlget(great):
with open("testforurl.html", encoding='UTF-8') as sm: #打开文件
        soup = BeautifulSoup(sm, 'html.parser', from_encoding = 'utf-8') #解析文件
content = str(soup.find('body'))

# for url in urlget: #输出url
fq = open("geta.html","a+",encoding='utf-8')
print(content)
fq.write(content)
fq.close()

# htmlget('test.html')

# def main(self)::
# getAlla.htmlget(great = 'test.html')
# print(HTMLClient.GetPage("","https://docs.ucloud.cn/security/uads/index"))

output = pypandoc.convert_file('testforurl.html', 'docx',outputfile="testforurl.docx")
assert output == ""

# self =''
# MYHTMLParser.__init__(self,docx.Document("d://a.docx"))
# print(self)