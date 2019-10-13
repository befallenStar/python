# -*- encoding: utf-8 -*-
import logging
'''
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
'''
'''
filename：指定日志文件名
filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'
format：指定输出的格式和内容，format可以输出很多有用的信息
datefmt：指定时间格式，同time.strftime()
level：设置日志级别，默认为logging.WARNNING
stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
'''


class TextLogging(object):
    def __init__(self):
        self.filename = "log.txt"
        self.format = "%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s"
        logging.basicConfig(level=logging.INFO, filename=self.filename,
                            format=self.format,filemode='w')


textLogging = TextLogging()
logging.critical("message")
logging.error("message")
logging.warning("message")
logging.info("message")
logging.debug("message")