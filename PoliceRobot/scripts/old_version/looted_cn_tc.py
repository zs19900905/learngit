import unittest
from time import sleep
from appium import webdriver

class TestLooted(unittest.TestCase):
    def testLootedA002(self):
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
        # 1、我被抢夺了
        sleep(2)
        looted = driver.find_element_by_xpath("//android.widget.TextView[@text='2.我被抢夺了']")
        looted.click()
        # 2、 阅读<行政案件义务告知书>
        sleep(1)
        reading_structions1 = driver.find_element_by_xpath("//android.widget.CheckBox[@text='我已阅读该告知书，并清楚告知书所有内容']").click()
        go_it_button1 = driver.find_element_by_xpath("//android.widget.Button[@text='清楚了']").click()
        sleep(1)
        # 3、 阅读<被害人诉讼权利义务告知书>
        reading_structions2 = driver.find_element_by_xpath("//android.widget.CheckBox[@text='我已阅读该告知书，并清楚告知书所有内容']").click()
        go_it_button2 = driver.find_element_by_xpath("//android.widget.Button[@text='清楚了']").click()
        # 4、 询问提示
        known_button = driver.find_element_by_xpath("//android.widget.TextView[@text='1.知道了']").click()
        # 5、询问是否携带身份证-选择“没有”
        no_id_card = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 6、输入名字
        ipt_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("B水蜜桃")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 7、录入身份证号
        ipt_id_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("421302199009056940")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 8、性别
        gender_button = driver.find_element_by_xpath("//android.widget.TextView[@text='2.女性']").click()
        # 9、民族
        ethnic_group = driver.find_element_by_xpath("//android.widget.TextView[@text='1.汉族']").click()
        # 10、出生日期
        date_birth = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 11、国籍
        nationality = driver.find_element_by_xpath("//android.widget.TextView[@text='1.中国']").click()
        # 12、户籍地址
        # province_city = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']")
        # province_city.click()
        # driver.swipe(349,882,351,888,1000)
        regisdence_address = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("高新园地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 13、居住地址
        current_address = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("高新园")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 14、职业
        job = driver.find_element_by_xpath("//android.widget.TextView[@text='5.公司职员']").click()
        # 15、教育水平
        edution_level = driver.find_element_by_xpath("//android.widget.TextView[@text='4.专科']").click()
        # 16、工作单位
        working_unit = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys('亿家智宝')
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 17、联系电话
        contact_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("18262991980")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 18、是否是人大代表
        npc_duty = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不是']").click()
        # 19、被抢夺窃地点
        looted_place = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("洪浪北地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 20、被抢夺窃发生时间
        start_time = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        confirm_button1 = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 21、被抢夺窃物品
        looted_article = driver.find_element_by_xpath("//android.widget.TextView[@text='1.机动车']").click()
        # 22、被抢夺窃具体车辆
        looted_vehicle = driver.find_element_by_xpath("//android.widget.TextView[@text='1.轿车']").click()
        # 23、被抢夺轿车品牌
        looted_car_brand = driver.find_element_by_xpath("//android.widget.TextView[@text='6.奥迪']").click()
        # 24、被抢夺轿车型号
        looted_car_model = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("AB1234")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 25、被抢夺轿车颜色
        stoen_car_color = driver.find_element_by_xpath("//android.widget.TextView[@text='5.蓝色']").click()
        # 26、被抢夺轿车车牌号码
        looted_car_license = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("粤B9876")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 27、被抢夺轿车的明显特征
        looted_car_feature = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("尾部贴有标签：新手上路，请保持车距。")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 28、被抢夺轿车是本人
        looted_car_own = driver.find_element_by_xpath("//android.widget.TextView[@text='1.是']").click()
        # 29 、被抢夺轿车的车架号
        looted_car_identificstion = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("chejiahao123")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 30、被抢夺轿车的发动机号
        looted_car_engine = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("fadongjihao123")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 31、可以提供驾驶证
        driving_license = driver.find_element_by_xpath("//android.widget.TextView[@text='2.可以提供']").click()
        # 32、被抢夺轿车没有到报废期
        retirement_date = driver.find_element_by_xpath("//android.widget.TextView[@text='1.没有']").click()
        # 33、没有将车借用过给他人
        no_lend_car = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 34、被抢夺轿车的购买日期
        purchase_date = driver.find_element_by_xpath("//android.widget.ImageView[@index='1']").click()
        confirm_time = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 35、被抢夺轿车的购买地点
        purchase_place = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：XX市XX区XX路XX商店，商场等']").send_keys("宝安汽车城")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 36、被抢夺轿车购买价格
        vehicle_price = driver.find_element_by_xpath("//android.widget.EditText[@text='提示：购买价格必须输入数字，从而方便计算价值']").send_keys("200000")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 37、被抢夺轿车新旧程度
        looted_car_condition = driver.find_element_by_xpath("//android.widget.TextView[@text='6.六成新']").click()
        # 38、可以提供购买票据
        purchase_bill = driver.find_element_by_xpath("//android.widget.TextView[@text='1.可以提供']").click()
        #39、无其它物品被抢夺
        no_other_looted = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无']").click()
        #40、在抢夺过程中没有受伤
        unjured = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 41、嫌疑人数量
        suspect_number = driver.find_element_by_xpath("//android.widget.TextView[@text='3.三个']").click()
        # 42、认识第一个嫌疑人
        cognizance_first_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='1.认识']").click()
        # 43、第一个嫌疑人的名字
        first_suspect_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("小A")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 44、第一个嫌疑人的性别
        first_suspect_gender = driver.find_element_by_xpath("//android.widget.TextView[@text='1.男性']").click()
        # 45、第一个嫌疑人的居住地址
        first_suspect_place = driver.find_element_by_xpath("//android.widget.Button[@text='不清楚']").click()
        # 46、第一个嫌疑人的联系电话
        first_suspect_telehone = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("16612345678")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 47、第一个嫌疑人的其它联系方式
        other_contact = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：QQXXXXXXX']").send_keys(" qq:1234567")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #48、第一个嫌疑人充当的角色
        first_suspect_role = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：主嫌犯，放哨人，诈骗托等等']").send_keys("放哨人")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #49、第一个嫌疑人没有使用工具离开现场
        no_instructions = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 50、第一个嫌疑人的逃跑路线
        escape_route = driver.find_element_by_xpath("//android.widget.Button[@text='不清楚']").click()
        #51、可以对第一嫌疑人进行辨认
        recognize_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='1.可以辨认']").click()
        #52、不认识第二个嫌疑人
        incognize_second_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不认识']").click()
        #53、第二个嫌疑人的性别
        second_suspect_gender = driver.find_element_by_xpath("//android.widget.TextView[@text='2.女性']").click()
        #54、第二个嫌疑人的口音
        second_suspect_accent = driver.find_element_by_xpath("//android.widget.Button[@text='没听清']").click()
        #55、第二个嫌疑人的身高
        second_suspect_height = driver.find_element_by_xpath("//android.widget.TextView[@text='4.一米八左右']").click()
        #56、第二个嫌疑人的头发颜色
        second_suspect_hair_color = driver.find_element_by_xpath("//android.widget.TextView[@text='6.黄色']").click()
        #57、第二个嫌疑人的发型
        second_suspect_hair_style = driver.find_element_by_xpath("//android.widget.TextView[@text='1.长发']").click()
        #58、第二个嫌疑人的身材
        second_suspect_figure = driver.find_element_by_xpath("//android.widget.TextView[@text='1.瘦']").click()
        #59、第二个嫌疑人身上的明显特征
        second_suspect_feature = driver.find_element_by_xpath("//android.widget.TextView[@text='3.有纹身']").click()
        #60、第二个嫌疑的着装
        second_suspect_dressing = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：XX帽子、XX外套、XXT恤、XX裤子、XX裙子等']").send_keys("白色短袖，黑色牛仔，戴有帽子。")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #61、第二个嫌疑人充当角色
        second_suspect_role = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：主嫌犯，放哨人，诈骗托等等']").send_keys("主嫌犯")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #62、第二个嫌疑人没有使用交通工具离开现场
        second_no_instructions = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        #63、第二个嫌疑人逃跑路线
        second_escape_route = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("往商场右拐角处跑了")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #64、无法对第二个嫌疑人辩认
        no_recognize_second_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无法辨认']").click()
        #65、不认识第三个嫌疑人
        no_see_third_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='3.没看清']").click()
        #66、有目击证人
        eyewitness = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        #67、有2个目击证人
        eyewitness_number = driver.find_element_by_xpath("//android.widget.TextView[@text='2.二个']").click()
        #68、认识第一个目击证人
        first_eyewitness = driver.find_element_by_xpath("//android.widget.TextView[@text='1.认识']").click()
        #69、第一个目击证人的姓名
        first_eyewitness_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("小可")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #70、第一个目击证人的性别
        first_witness_gender = driver.find_element_by_xpath("//android.widget.TextView[@text='1.男性']").click()
        #71、第一个目击证人的现居住地址
        first_eyewitness_place = driver.find_element_by_xpath("//android.widget.ImageView[@index='5']").click()
        ipt_place = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("西丽")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #72、第一个目击证人的联系电话
        first_eyewitness_telephone = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("18200000000")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #73、不认识第二个目击证人
        second_witness = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不认识']").click()
        #74、第二个目击证人的性别
        second_witness_gender = driver.find_element_by_xpath("//android.widget.TextView[@text='2.女性']").click()
        #75、第二个目击证人的口音
        second_witness_accent = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：粤语，普通话等']").send_keys("广东话")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #76、第二个目击证人的身高
        second_witness_height = driver.find_element_by_xpath("//android.widget.TextView[@text='7.一米六五左右']").click()
        #77、第二个目击证人的头发颜色
        second_witness_hair_color = driver.find_element_by_xpath("//android.widget.TextView[@text='6.黄色']").click()
        #78、第二个目击证人的发型
        second_witness_har_style = driver.find_element_by_xpath("//android.widget.TextView[@text='7.卷发']").click()
        #79、第二个目击证人的身材
        second_witness_figure = driver.find_element_by_xpath("//android.widget.TextView[@text='3.中等']").click()
        #80、第二个目击证人的特征
        second_witness_feature = driver.find_element_by_xpath("//android.widget.TextView[@text='3.有纹身']").click()
        #81、第二个目击证人的着装
        second_witness_dressing = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：XX帽子、XX外套、XXT恤、XX裤子、XX裙子等']").send_keys("白色T恤，黑色牛仔短裤，小白鞋")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #82、有监控录像
        surveillance_vide = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有监控录像']").click()
        #83、监控位置
        camera_position = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("大楼拐角处和侧面")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #84、有可疑线索
        clue = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有可疑线索']").click()
        #85、线索内容
        clue_content = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("落下了一双白色手套")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #86、对报案有补充
        have_add = driver.find_element_by_xpath("//android.widget.TextView[@text='1.我有补充']").click()
        #87、补充内容
        supplementary_information = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("在大楼周围晃悠了几圈，去便利店买了瓶水")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #88、提交
        submit = driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        #89、属实
        true_button = driver.find_element_by_xpath("//android.widget.Button[@text='属实']").click()

        sleep(3)
        driver.quit()
if __name__ == '__main__':
    unittest.main()

