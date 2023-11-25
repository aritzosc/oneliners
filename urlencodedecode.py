#!/usr/bin/env python3

import urllib
import urllib.parse

class UrlUtil:
    def __init__(self, classname):
        self.classname = classname

    def url_encode(self, url):
        return urllib.parse.quote_plus(url)

    def url_decode(self,url):
        return urllibr.parse.unquote_plush(url)
