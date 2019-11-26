#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 22:29
# @Author  : KevinLi
# @Email   : 623620767@qq.com
# @File    : main.py
# @Software: PyCharm

import os
import sys
import logging
from utils import MySqlHelpter
from utils import config

Logger = logging.getLogger('MonitorLog')

mysqlConfig = config.getConfigDictBySink("mysql-test")
mysqlConfig = MySqlHelpter(mysqlConfig)