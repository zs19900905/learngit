import unittest
from time import sleep
from appium import webdriver

class TestDamaged(unittest.TestCase):
    def testDamagedA006(self):
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
        # 1、我的财务被故意损毁
        stolen = driver.find_element_by_xpath("//android.widget.TextView[@text='5.我的财物被故意损毁']").click()
        # 2、清楚的损失价值
        damaged_value = driver.find_element_by_xpath("//android.widget.TextView[@text='1.清楚']").click()
        # 3、损失价值范围
        value_range = driver.find_element_by_xpath("//android.widget.TextView[@text='1.损失大于等于5000']").click()
        sleep(1)
        # 3、 阅读<被害人诉讼权利义务告知书>
        reading_structions2 = driver.find_element_by_xpath("//android.widget.CheckBox[@text='我已阅读该告知书，并清楚告知书所有内容']").click()
        go_it_button2 = driver.find_element_by_xpath("//android.widget.Button[@text='清楚了']").click()
        # 4、 询问提示
        known_button = driver.find_element_by_xpath("//android.widget.TextView[@text='1.知道了']").click()
        # 5、询问是否携带身份证-选择“没有”
        no_id_card = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 6、输入名字
        ipt_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("F红提")
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
        # 19、被损毁地点
        stolen_place = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("洪浪北地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 20、被损毁发生时间
        start_time = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        confirm_button1 = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 21、被损毁物品
        stolen_article = driver.find_element_by_xpath("//android.widget.TextView[@text='1.机动车']").click()
        # 22、被损毁具体车辆
        stolen_vehicle = driver.find_element_by_xpath("//android.widget.TextView[@text='1.轿车']").click()
        # 23、被损毁轿车品牌
        stolen_car_brand = driver.find_element_by_xpath("//android.widget.TextView[@text='6.奥迪']").click()
        # 24、被损毁轿车型号
        stolen_car_model = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("AB1234")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 25、被损毁轿车颜色
        stoen_car_color = driver.find_element_by_xpath("//android.widget.TextView[@text='5.蓝色']").click()
        # 26、被损毁轿车车牌号码
        stolen_car_license = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("粤B9876")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 27、被损毁轿车的部位
        damaged_area = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：车身']").send_keys("车后视镜")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #被损毁部位的价值
        damaged_value = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：1500元']").send_keys("2500")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 28、被损毁轿车是本人
        stolen_car_own = driver.find_element_by_xpath("//android.widget.TextView[@text='1.是']").click()
        # 29、被损毁轿车的购买日期
        purchase_date = driver.find_element_by_xpath("//android.widget.ImageView[@index='1']").click()
        confirm_time = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 30、被损毁轿车的购买地点
        purchase_place = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：XX市XX区XX路XX商店，商场等']").send_keys("宝安汽车城")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 31、被损毁轿车购买价格
        vehicle_price = driver.find_element_by_xpath("//android.widget.EditText[@text='提示：购买价格必须输入数字，从而方便计算价值']").send_keys("200000")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 32、被损毁轿车新旧程度
        stolen_car_condition = driver.find_element_by_xpath("//android.widget.TextView[@text='6.六成新']").click()
        # 33、可以提供购买票据
        purchase_bill = driver.find_element_by_xpath("//android.widget.TextView[@text='1.可以提供']").click()
        # 34、无其它物品被损毁
        no_other_stolen = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无']").click()
        # 37、案发时是否在现场
        on_the_scene = driver.find_element_by_xpath("//android.widget.TextView[@text='1.在现场']").click()
        # 38、损坏方式
        damage_way = driver.find_element_by_xpath("//android.widget.TextView[@text='4.打砸']").click()
        # 39、使用何种工具
        use_tool = driver.find_element_by_xpath("//android.widget.TextView[@text='1.石头砖头']").click()
        # 40、工具的特征
        tool_feature = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：长XXcm 、宽XXcm']").send_keys("圆形大理石")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 41、请问工具是谁带来的
        tool_origin = driver.find_element_by_xpath("//android.widget.TextView[@text='1.在现场的工具']").click()
        # 42、工具在何处
        tool_place = driver.find_element_by_xpath("//android.widget.TextView[@text='1.在现场']").click()
        # 43、是否还通过其他方式损坏
        other_damage_way = driver.find_element_by_xpath("//android.widget.TextView[@text='2.否']").click()
        #54、有使用暴力相威胁
        threatened = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        #55、使用何种暴力威胁
        threatened_type = driver.find_element_by_xpath("//android.widget.EditText[@text=' 例如：殴打、捆绑、禁锢，用刀捅伤我或恐吓不听我的，我就杀了你等']").send_keys("不答应我就杀了你")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #56、在抢劫过程中有使用工具
        robbed_instrument = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有使用工具']").click()
        #57、使用工具：刀
        use_knife = driver.find_element_by_xpath("//android.widget.TextView[@text='1.刀']").click()
        #58、刀的类型
        knife_type = driver.find_element_by_xpath("//android.widget.TextView[@text='1.匕首']").click()
        #59、刀的特征
        knife_feature = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：刀柄长XXcm  刀身长XXcm']").send_keys("长20厘米，刀柄黑色")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #60、工具是对方带来的
        knife_brought = driver.find_element_by_xpath("//android.widget.TextView[@text='2.对方带来的工具']").click()
        #61、工具被嫌疑人带走了
        tool_taken_away = driver.find_element_by_xpath("//android.widget.TextView[@text='2.被嫌疑人带走了']").click()
        #62、对方没有使用其它工具
        no_other_tools = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        ############################数字没有衔接上#########################################333
        #40、在抢劫过程中没有受伤
        unjured = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 41、嫌疑人数量
        suspect_number = driver.find_element_by_xpath("//android.widget.TextView[@text='3.三个']").click()
        # 42、认识第一个嫌疑人
        cognizance_first_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='1.认识']").click()
        # 43、第一个嫌疑人的名字
        first_suspect_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("小A")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 44、第一个嫌疑人的性别
        first_suspect_gender = driver.find_element_by_xpath("//android.widget.TextView[@text='1.男性']").click()
        # 45、第一个嫌疑人的居住地址
        first_suspect_place = driver.find_element_by_xpath("//android.widget.Button[@text='不清楚']").click()
        # 46、第一个嫌疑人的联系电话
        first_suspect_telehone = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("16612345678")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        # 47、第一个嫌疑人的其它联系方式
        other_contact = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：QQXXXXXXX']").send_keys(" qq:1234567")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #48、第一个嫌疑人充当的角色
        first_suspect_role = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：主嫌犯，放哨人，诈骗托等等']").send_keys("放哨人")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
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
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #61、第二个嫌疑人充当角色
        second_suspect_role = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：主嫌犯，放哨人，诈骗托等等']").send_keys("主嫌犯")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #62、第二个嫌疑人没有使用交通工具离开现场
        second_no_instructions = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        #63、第二个嫌疑人逃跑路线
        second_escape_route = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("往商场右拐角处跑了")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #64、无法对第二个嫌疑人辩认
        no_recognize_second_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无法辨认']").click()
        #65、不认识第三个嫌疑人
        no_see_third_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='3.没看清']").click()
        # 请问案发现场是否有遗留涉案物品
        falling_objects = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有遗留涉案物品']").click()
        # 现场遗留涉案物品情况
        object_condition = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：遗留了铁棍一根']").send_keys("遗留了一双手套")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #66、有监控录像
        surveillance_vide = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有监控录像']").click()
        #67、监控位置
        camera_position = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("大楼拐角处和侧面")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        #68、有可疑线索
        clue = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有可疑线索']").click()
        #69、线索内容
        clue_content = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("落下了一双白色手套")
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