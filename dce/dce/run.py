#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2017/1/1 17:51
# @Author : lzh
from scrapy import cmdline

name = 'dceDay'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
