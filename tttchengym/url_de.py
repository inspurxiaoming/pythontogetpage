# coding:utf-8
import urllib.parse


class Urlchuli():
    """Url处理类，需要传入两个实参：Urlchuli('实参','编码类型')，默认utf-8
    url编码方法：url_bm() url解码方法：url_jm()"""

    def __init__(self,can,mazhi='utf-8'):
        self.can = can
        self.mazhi = mazhi

    def url_bm(self):
        """url_bm() 将传入的中文实参转为Urlencode编码"""
        quma = str(self.can).encode(self.mazhi)
        bianma = urllib.parse.quote(quma)
        return bianma

    def url_jm(self):
        """url_jm() 将传入的url进行解码成中文"""
        quma = str(self.can)
        jiema = urllib.parse.unquote(quma,self.mazhi)
        return jiema