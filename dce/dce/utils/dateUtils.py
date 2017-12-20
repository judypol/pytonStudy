#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time


class DateUtils:
    # 按指定的格式，格式化字符串
    @staticmethod
    def getDateString(date=None, formate=None):

        if date is None:
            date = time.localtime()
        if formate is None:
            formate = '%Y-%m-%d'

        date = time.strftime(formate, date)
        return date

    # 按指定的格式，格式化字符串
    @staticmethod
    def getDateTimeString(date=None, formate=None):
        if date is None:
            date = time.localtime()
        if formate is None:
            formate = '%Y-%m-%d %H:%M:%S'

        stringTime = time.strftime(formate, date)
        return stringTime
