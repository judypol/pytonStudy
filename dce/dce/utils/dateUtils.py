#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time


class dateUtils:
    # 获取当前日期的字符串
    @staticmethod
    def getDateString():
        localDate = time.strftime("%Y-%m-%d", time.localtime())
        return localDate

    # 获取当前时间的字符串
    @staticmethod
    def getDateTime():
        localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return localTime

    # 按指定的格式，格式化字符串
    @staticmethod
    def getDateString(date, formate):
        date = time.strftime(formate, date)
        return date

    # 按指定的格式，格式化字符串
    @staticmethod
    def getDateTimeString(date, formate):
        stringTime = time.strftime(formate, date)
        return stringTime
