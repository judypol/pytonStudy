#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urlparse


class UrlUtils:
    @staticmethod
    def getQueryValue(url, key):
        query = urlparse.urlparse(url).query
        return urlparse.parse_qs(query).get(key)[0]
