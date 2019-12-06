import unittest
from time import sleep
from appium import webdriver

class TestTelecommunicationFraud(unittest.TestCase):
    def testTelecommunicationFraudA004(self):
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
        #返回到主界面
        home_page_button = driver.find_element_by_xpath("//android.widget.Button[@text='首页']").click()
        #我要报案
        report_case = driver.find_element_by_xpath("//android.widget.Button[@text='我要报案']").click()
        # 1、我被诈骗了
        cheated = driver.find_element_by_xpath("//android.widget.TextView[@text='4.我被诈骗了']").click()
        #2、电信诈骗
        telecommunication_frad = driver.find_element_by_xpath("//android.widget.TextView[@text='1.电信诈骗']").click()
        sleep(1)
        # 3、 阅读<行政案件义务告知书>
        reading_structions1 = driver.find_element_by_xpath("//android.widget.CheckBox[@text='我已阅读该告知书，并清楚告知书所有内容']").click()
        go_it_button1 = driver.find_element_by_xpath("//android.widget.Button[@text='清楚了']").click()
        sleep(1)
        # 4、 阅读<被害人诉讼权利义务告知书>
        reading_structions2 = driver.find_element_by_xpath("//android.widget.CheckBox[@text='我已阅读该告知书，并清楚告知书所有内容']").click()
        go_it_button2 = driver.find_element_by_xpath("//android.widget.Button[@text='清楚了']").click()
        # 5、 询问提示
        known_button = driver.find_element_by_xpath("//android.widget.TextView[@text='1.知道了']").click()
        # 6、询问是否携带身份证-选择“没有”
        no_id_card = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 7、输入名字
        ipt_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("D菠萝")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 8、录入身份证号
        ipt_id_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("421302199009056940")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 9、性别
        gender_button = driver.find_element_by_xpath("//android.widget.TextView[@text='2.女性']").click()
        # 10、民族
        ethnic_group = driver.find_element_by_xpath("//android.widget.TextView[@text='1.汉族']").click()
        # 11、出生日期
        date_birth = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 12、国籍
        nationality = driver.find_element_by_xpath("//android.widget.TextView[@text='1.中国']").click()
        # 13、户籍地址
        # province_city = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']")
        # province_city.click()
        # driver.swipe(349,882,351,888,1000)
        regisdence_address = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("高新园地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 14、居住地址
        current_address = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("高新园")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 15、职业
        job = driver.find_element_by_xpath("//android.widget.TextView[@text='5.公司职员']").click()
        # 16、教育水平
        edution_level = driver.find_element_by_xpath("//android.widget.TextView[@text='4.专科']").click()
        # 17、工作单位
        working_unit = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys('亿家智宝')
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 18、联系电话
        contact_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("18262991980")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 19、是否是人大代表
        npc_duty = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不是']").click()
        # 20、被诈骗地点
        cheated_place = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("洪浪北地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 21、被诈骗发生时间
        start_time = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        confirm_button1 = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #22、被诈骗的金额
        cheated_amount = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("5000")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #23、被诈骗的方式
        cheated_way =  driver.find_element_by_xpath("//android.widget.TextView[@text='1.扫描二维码植入木马诈骗']").click()
        #24、不是使用同一种方式多次转账
        transfer_way = driver.find_element_by_xpath("//android.widget.TextView[@text='2.否']").click()
        #25、支付了2次
        pay_times = driver.find_element_by_xpath("//android.widget.TextView[@text='2.二次']").click()
        #26、第一次支付--银行卡转账
        first_pay = driver.find_element_by_xpath("//android.widget.TextView[@text='1.银行转账']").click()
        #27、转账时银行卡号
        bank_account = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("333222444555666777")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #28、支付银行开户行
        deposit_bank = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("招商银行深圳高新园支行")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #29、支付银行开户名
        account_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("小Q")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #30、第一次支付时对方收钱的银行名称
        receive_bank = driver.find_element_by_xpath("//android.widget.TextView[@text='2.中国建设银行']").click()
        #31、收钱的账号
        receive_account = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("999888777666555")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #32、对方收钱银行卡的开户名
        receive_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("小W")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #33、能提供转账凭证
        transfer_voucher = driver.find_element_by_xpath("//android.widget.TextView[@text='1.能']").click()
        #34、第二次支付
        second_pay = driver.find_element_by_xpath("//android.widget.TextView[@text='2.微信转账']").click()
        #35、请问第二次转账的使用微信号或名称
        transfer_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("xixi123")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #36、第二次转账时收钱账号、昵称
        receive_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("haha456")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #37、不能提供转账记录
        transfer_voucher = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不能']").click()
        #38、描述电信诈骗的具体过程
        cheated_way = driver.find_element_by_xpath("//android.widget.EditText[@text='例如:XX时间在XX地点我和XX(嫌疑人)如何认识,XX(嫌疑人)通过什么手段使我受骗']").send_keys("2019年6月20日在通过微信认识，在网上卖东西，钱付了没发货")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #39、嫌疑人联系我的主要方式
        contact_way = driver.find_element_by_xpath("//android.widget.TextView[@text='2.微信']").click()
        #40、嫌疑人的账号和昵称
        suspect_information = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("lala123,时尚达人")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #41、请问否还通过其它方式联系你
        other_contact_way = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有其他方式']").click()
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