#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy import cmdline

name = 'sinahq'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
