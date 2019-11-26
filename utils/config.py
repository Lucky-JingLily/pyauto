#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 22:29
# @Author  : KevinLi
# @Email   : 623620767@qq.com
# @File    : config.py
# @Software: PyCharm

import configparser
import os
import sys

def getConfigDictByService(service):
	configDict = {}
	config = configparser.ConfigParser()
	configPath = os.path.join(sys.path[0], 'config/%s.cfg'%service)
	config.read(configPath)
	for cluster in config.sections():
		conf = config._sections[cluster]
		configDict[cluster] = conf
	return configDict

def getConfigDictBySink(sink):
	configDict = {}
	config = configparser.ConfigParser()
	configPath = os.path.join(sys.path[0], 'config/sinks.cfg')
	config.read(configPath)
	if sink in config.sections():
		configDict = config._sections[sink]
	return configDict

