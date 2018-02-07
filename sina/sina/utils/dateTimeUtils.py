#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime


class DateTimeUtils:
    @staticmethod
    def getNow():
        return datetime.datetime.now()

    @staticmethod
    def getStartTime():
        nowTime = datetime.datetime.now()
        return nowTime.strftime('%Y%m%d%H%M') + '00'

    @staticmethod
    def getContractList():
        contractList = []
        nowDate = datetime.datetime.today()
        contractList.append(nowDate.strftime('%y%m'))
        nowYear = nowDate.year
        nowMonth = nowDate.month
        for num in range(1, 13):
            month = nowMonth + num
            if month > 12:
                month = month - 12
                year = nowYear + 1
            else:
                month = month
                year = nowYear
            tmpDate = datetime.datetime(year=year, month=month, day=1)
            contractList.append(tmpDate.strftime('%y%m'))

        return contractList
