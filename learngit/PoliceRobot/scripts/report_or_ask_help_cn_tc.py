import unittest
from time import sleep
from appium import webdriver

class TestReport(unittest.TestCase):
    def testReportOrHelpA012(self):
        dc = {}
        dc['automationName'] = 'Uiautomator2'
        dc['platformName'] = 'Android'
        dc['platformVersion'] = '5.1.1'
        dc['deviceName'] = '127.0.0.1:52001'
        dc['udid'] = '127.0.0.1:52001'
        dc['appPackage'] = 'com.kv.baoanrobot'
        dc['appActivity'] = 'com.kv.baoanrobot.activity.WelcomeActivity'
        dc['app'] = r'C:\Users\技嘉\Desktop\kv\kv_app-debug.apk'
        dc['newCommandTimeOut'] = 60

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',dc)
        driver.implicitly_wait(30)

        #设置
        setting_button = driver.find_element_by_xpath("//android.widget.Button[@text='设置']").click()
        #输入账号
        ipt_username = driver.find_element_by_xpath("//android.widget.EditText[@text='用户名']").send_keys('admin')
        ipt_password = driver.find_element_by_xpath("//android.widget.EditText[@index='3']").send_keys('admin')
        login_button = driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        #通用设置
        general_setting = driver.find_element_by_xpath("//android.widget.Button[@text='通用设置']").click()
        #宣读时间
        reading_time = driver.find_element_by_xpath("//android.widget.EditText[@text='10']").clear()
        reading_time.send_keys('1')
        # #打开录屏
        # close_viedo = driver.find_element_by_id("com.kv.baoanrobot:id/video_recording_switch").click()
        #返回到主界面
        home_page_button = driver.find_element_by_xpath("//android.widget.Button[@text='首页']").click()
        #我要报案
        report_case = driver.find_element_by_xpath("//android.widget.Button[@text='我要报案']").click()
        # 1、其它案件
        persecuted = driver.find_element_by_xpath("//android.widget.TextView[@text='7.其他案件']").click()
        # 2、我要反映情况或求助
        beatened = driver.find_element_by_xpath("//android.widget.TextView[@text='4.我要反映情况或求助']").click()
        # 4、 询问提示
        known_button = driver.find_element_by_xpath("//android.widget.TextView[@text='1.知道了']").click()
        # 5、询问是否携带身份证-选择“没有”
        no_id_card = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 6、输入名字
        ipt_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("L樱桃")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 7、录入身份证号
        ipt_id_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("421302199009056940")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 8、性别
        gender_button = driver.find_element_by_xpath("//android.widget.TextView[@text='2.女性']").click()
        # 9、民族
        ethnic_group = driver.find_element_by_xpath("//android.widget.TextView[@text='1.汉族']").click()
        # 10、出生日期
        date_birth = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 11、国籍
        nationality = driver.find_element_by_xpath("//android.widget.TextView[@text='1.中国']").click()
        # 12、户籍地址
        # province_city = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']")
        # province_city.click()
        # driver.swipe(349,882,351,888,1000)
        regisdence_address = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("高新园地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 13、居住地址
        current_address = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("高新园")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 14、职业
        job = driver.find_element_by_xpath("//android.widget.TextView[@text='5.公司职员']").click()
        # 15、教育水平
        edution_level = driver.find_element_by_xpath("//android.widget.TextView[@text='4.专科']").click()
        # 16、工作单位
        working_unit = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys('亿家智宝')
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 17、联系电话
        contact_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("18262991980")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 18、是否是人大代表
        npc_duty = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不是']").click()
        # 18、请问具体因何事来公安机关
        report_reason = driver.find_element_by_xpath("//android.widget.TextView[@text='1.反映情况']").click()
        # 19、请问您反映何种情况
        reflect_situation = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("有贪污受贿")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 20、被找麻烦发生时间
        start_time = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        confirm_button1 = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 19、被找麻烦地点
        persecuted_place = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("洪浪北地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 22、请问因何事引起
        reason = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("交的活动资金不知道去哪儿了")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 23、请问反映事件的详细经过
        detail_happen = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("前不久公司动员大家每人交钱说是搞公益活动，结果真需要办活动的时候说没钱")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 24、请问有何看法
        opinion = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("这个事情很严肃，需要调查清楚，不能助长不良风气。")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #66、有监控录像
        surveillance_vide = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有监控录像']").click()
        #67、监控位置
        camera_position = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("大楼拐角处和侧面")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #70、对报案有补充
        have_add = driver.find_element_by_xpath("//android.widget.TextView[@text='1.我有补充']").click()
        #71、补充内容
        supplementary_information = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("在大楼周围晃悠了几圈，去便利店买了瓶水")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #72、提交
        submit = driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        #73、属实
        true_button = driver.find_element_by_xpath("//android.widget.Button[@text='属实']").click()

        sleep(3)
        driver.quit()
if __name__ == '__main__':
    unittest.main()











