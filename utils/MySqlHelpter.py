#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 22:13
# @Author  : KevinLi
# @Email   : 623620767@qq.com
# @File    : MySqlHelpter.py
# @Software: PyCharm

import logging
import pymysql
pymysql.install_as_MySQLdb()

logger = logging.getLogger('MonitorLog')

class MysqlServer(object):
    """连接Mysql数据服务器 """

    def __init__(self, db_config):
        try:
            self._db_config = db_config
            self._conn = self.__get_conn()
            self._cursor = self._conn.cursor()
            logger.info("数据库连接正常")
        except Exception:
            self.close()
            logger.error(u"ret=1,res=连接数据库异常,请检查数据库是否正常!")

    def __get_conn(self):
        try:
            db_config = self._db_config
            connection = pymysql.connect(host=db_config['mysql.host'], port=db_config['mysql.port'], user=db_config['mysql.username'],
                                     passwd=db_config['mysql.password'], db=db_config['mysql.database'], charset="utf8")
            connection.ping(True)
            return connection
        except Exception as e:
            logger.error(u"ret=1,res=连接数据库异常,请尽快处理")

    def ensure_cursor(self):
        if not self._cursor:
            if not self._conn:
                self._conn = self.__get_conn()
            self._cursor = self._conn.cursor()

    def run_sql(self, sql):
        self.ensure_cursor()
        self._cursor.execute(sql)
        #commit只对innodb生效，不加commit的话，修改数据库记录的操作不会生效。而如果是myisam引擎的话，不需要commit即可生效
        self._conn.commit()
        return self._cursor.fetchall()

    def execute_sql(self, sql):
        try:
            self.ensure_cursor()
            self._cursor.execute(sql)
            self._conn.commit()
            return True
        except Exception as e:
            return False


    def run_sql_fetchone(self, sql):
        self.ensure_cursor()
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()
