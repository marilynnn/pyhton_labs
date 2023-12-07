import enum
import time

def gettime():
    return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())


class Singleton:
    ''' класс, реализующий шаблон Singleton '''
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class LogMsgType(enum.Enum):
    ''' Перечень типов сообщений для логирования '''
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    CRITICAL = 4

class Logger(Singleton):

    def __new__(cls, *args, **kwargs ):
        instance = super().__new__(cls)
        return instance

    def __init__(self, logname):
        self.logfile = open(logname, 'w')

    def __del__(self):
        self.logfile.close()

    def __logMsg(self, msg_type, msg):
        msg_time = gettime()
        print(f"[{msg_type.name}] {msg_time} : {msg} \n", file=self.logfile)

    def debug_msg(self, msg):
        ''' Добавление в лог сообщений типа DEBUG'''
        self.__logMsg(LogMsgType.DEBUG, msg)

    def info_msg(self, msg):
        ''' Добавление в лог сообщений типа INFO'''
        self.__logMsg(LogMsgType.INFO, msg)

    def warn_msg(self, msg):
        ''' Добавление в лог сообщений типа WARN'''
        self.__logMsg(LogMsgType.WARN, msg)

    def error_msg(self, msg):
        ''' Добавление в лог сообщений типа ERROR'''
        self.__logMsg(LogMsgType.ERROR, msg)

    def critical_msg(self, msg):
        ''' Добавление в лог сообщений типа CRITICAL'''
        self.__logMsg(LogMsgType.CRITICAL, msg)

l = Logger('mylog.txt')
msg = "test_msg"
l.info_msg(msg)
