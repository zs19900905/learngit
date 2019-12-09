
import unittest
import time
from HTMLTestReport import HTMLTestRunner


dirpath = './scripts'
discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
currenttime = time.strftime('%y%m%d%H%M%S ')
filedir = './reports/' + 'report' + currenttime + '.html'
fp = open(filedir,'wb')
runner = HTMLTestRunner(stream=fp,
                        title=u'警务机器人自动化测试报告',
                        description=u'警务机器人自动化报案流程',
                        tester = u"赵珊",verbosity=2 )
runner.run(discover)
fp.close()



