from bs4 import BeautifulSoup #导入模块
def htmlget(great):
    with open(great,encoding='utf-8') as sm: #打开文件
        soup = BeautifulSoup(sm, 'html.parser', from_encoding = 'utf-8') #解析文件
    urlget = soup.find_all('a') #获取url
    for url in urlget: #输出url
        fq = open("allafromtestforurl.txt", "a+", encoding='utf-8')
        print(url['href'])
        fq.writelines(url['href']+"\n")
        fq.close()
# if __name == '__main__': #主函数
#     htmlget(great = 'test.html')
htmlget(great = 'testforurl.html')