#!/usr/bin/env python
# coding: utf-8
# Listen Mysql Run

import mysql.connector 
from mysql.connector import errorcode
import telnetlib

class SlaveStatu:
    __instance__ = None
    __error__ = []

    def __init__(self,):
        self.__config__ = {
            "host":"localhsot",
            "user":"root",
            "password":"admin888",
            "port":3306,
        }

    def __configParseMySQL__(self):
        return {
            "host"     : self.__config__["host"],
            "port"     : self.__config__["port"],
            "user"     : self.__config__["user"],
            "password" : self.__config__["password"]
        }

    def telnet( self, host, port, timeout=5 ):
        """
                测试服务器地址和端口是否畅通
        :param host: 服务器地址
        :param port: 服务器端口
        :param timeout: 测试超时时间
        :return: Boolean
        """
        try:
            tel = telnetlib.Telnet( host, port, timeout )
            tel.close()
            return True
        except:
            return False

    def connect(self):
        """
                创建数据库链接
        """
        try:
            config = self.__configParseMySQL__()
            if self.telnet( config["host"],config["port"]):
                self.__instance__ = mysql.connector.connect( **config )
                return True
            else:
                raise Exception("unable connect")
        except:
            self.__error__.append( "无法连接服务器主机: {host}:{port}".format( host=config[
                    "host"], port=config["port"]) )
            return False

    def isSlave(self):
        """
                数据库同步是否正常
        :return: None同步未开启,False同步中断,True同步正常
        """
        cur = self.__instance__.cursor(dictionary=True)
        cur.execute("SHOW SLAVE STATUS")
        result = cur.fetchone()
        cur.close()

        if result:
            if result["Slave_SQL_Running"] == "Yes" and result["Slave_IO_Running"] == "Yes":
                return True
            else:
                if result["Slave_SQL_Running"] == "No":
                    self.__error__.append( result["Last_SQL_Error"] )
                else:
                    self.__error__.append( result["Last_IO_Error"] )
                return False

    def get_last_error(self):
        """
                获取第一个错误信息
        :return: String
        """
        if self.__error__:
            return self.__error__.pop(0)

    def close(self):
        """
                关闭数据库链接
        """
        if self.__instance__:
            self.__instance__.close()


if __name__ == "__main__":
    Statu = SlaveStatu()
    Statu.close()



