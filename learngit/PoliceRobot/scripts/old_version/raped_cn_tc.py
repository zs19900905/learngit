import unittest
from time import sleep
from appium import webdriver

class TestRaped(unittest.TestCase):
    def testRapedA011(self):
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
        # 1、其它案件
        persecuted = driver.find_element_by_xpath("//android.widget.TextView[@text='7.其他案件']").click()
        # 2、我被强奸了
        beatened = driver.find_element_by_xpath("//android.widget.TextView[@text='3.我被强奸了']").click()
        # 3、 阅读<被害人诉讼权利义务告知书>
        reading_structions2 = driver.find_element_by_xpath("//android.widget.CheckBox[@text='我已阅读该告知书，并清楚告知书所有内容']").click()
        go_it_button2 = driver.find_element_by_xpath("//android.widget.Button[@text='清楚了']").click()
        # 4、 询问提示
        known_button = driver.find_element_by_xpath("//android.widget.TextView[@text='1.知道了']").click()
        # 5、询问是否携带身份证-选择“没有”
        no_id_card = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 6、输入名字
        ipt_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("K柚子")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 7、录入身份证号
        ipt_id_number = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("421302199009056940")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
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
        # 19、被找麻烦地点
        persecuted_place = driver.find_element_by_xpath("//android.widget.EditText[@text='点击输入内容']").send_keys("洪浪北地铁站")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 20、被找麻烦发生时间
        start_time = driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
        confirm_button1 = driver.find_element_by_id("com.kv.baoanrobot:id/btnSubmit").click()
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #20、请问您在被强奸之前是否喝过什么东西
        drink = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        # 21、请问您喝了什么东西
        drink_thing = driver.find_element_by_xpath("//android.widget.TextView[@text='1.水']").click()
        # 22、请问饮品中是否有添加物质
        add_thing = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        # 23、请问饮品中有加何种物质
        drink_something = driver.find_element_by_xpath("//android.widget.TextView[@text='1.类似药丸/药粉']").click()
        # 26、请问嫌疑人实施猥亵过程中有否使用暴力或者以暴力相威胁
        threatened = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        #55、使用何种暴力威胁
        threatened_type = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：殴打、捆绑、禁锢，用刀捅伤我或恐吓不听我的，我就杀了你等']").send_keys("听指挥就是了，不答应就杀了你")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #56、在抢劫过程中有使用工具
        robbed_instrument = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有使用工具']").click()
        #57、使用工具：刀
        use_knife = driver.find_element_by_xpath("//android.widget.TextView[@text='1.刀']").click()
        #58、刀的类型
        knife_type = driver.find_element_by_xpath("//android.widget.TextView[@text='1.匕首']").click()
        #59、刀的特征
        knife_feature = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：刀柄长XXcm  刀身长XXcm']").send_keys("长20厘米，刀柄黑色")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #60、工具是对方带来的
        knife_brought = driver.find_element_by_xpath("//android.widget.TextView[@text='2.对方带来的工具']").click()
        #61、工具被嫌疑人带走了
        tool_taken_away = driver.find_element_by_xpath("//android.widget.TextView[@text='2.被嫌疑人带走了']").click()
        #62、对方没有使用其它工具
        no_other_tools = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        #29、请问你在殴打过程中有否受伤
        injured = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        # 30、请问你的受作部位是哪里
        injured_part = driver.find_element_by_xpath("//android.widget.TextView[@text='7.鼻子']").click()
        # 31、伤势如何
        injured_situation = driver.find_element_by_xpath("//android.widget.TextView[@text='2.流血']").click()
        # 32、伤口情况
        wounds = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：流血需描述伤口长XX厘米   面积为XX平方厘米']").send_keys("流血不止")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 33、请问能否分辨伤处是对方以什么动作造成的
        how_lead = driver.find_element_by_xpath("//android.widget.TextView[@text='1.我能分辨']").click()
        # 34、请问伤处是对方以什么动作造成
        action = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：踢了我两脚']").send_keys("打了两拳")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 35、请问受途部位以前有没有受过伤
        unbeatened_before = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有受过伤']").click()
        # 36、请问是否有其他部位受伤
        no_other_beatened = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 37、请问是否有到医院治疗
        see_doctor = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        # 38、请问能否提供医院的病历和诊断证明
        provide_proof = driver.find_element_by_xpath("//android.widget.TextView[@text='1.能']").click()
        # 64、请问是否有还手
        strike_back = driver.find_element_by_xpath("//android.widget.TextView[@text='1.是']").click()
        # 65、请问通过何种方式还手
        strike_back_way = driver.find_element_by_xpath("//android.widget.TextView[@text='1.徒手（拳打脚踢）']").click()
        # 66、徒手反抗情况
        strike_back_situation = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：  推打、抓、咬等']").send_keys("用手推打")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 67、请问对方有没有受伤
        other_beaten_situation = driver.find_element_by_xpath("//android.widget.TextView[@text='3.不清楚']").click()
        # 41、嫌疑人数量
        suspect_number = driver.find_element_by_xpath("//android.widget.TextView[@text='2.二个']").click()
        # 42、认识第一个嫌疑人
        cognizance_first_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='1.认识']").click()
        # 43、第一个嫌疑人的名字
        first_suspect_name = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("在网上玩游戏认识的")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
         # 50、请问第一个嫌疑人的身份信息
        identify_information = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：姓名：XXX,男，xx人、年约xx岁，手机号、QQ、微信号等']").send_keys("小C,男，32岁，手机号17712345678，微信号6254634")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 51、请问双方是什么关系
        relationship = driver.find_element_by_xpath("//android.widget.TextView[@text='3.网友']").click()
        # 52、请问您之前是否有与其发生过性关系
        sexual = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        # 53、请问您能否辩认出第一个嫌疑人
        distinguish_first = driver.find_element_by_xpath("//android.widget.TextView[@text='1.能']").click()
        # 54、请问您认不认识第二个嫌疑人
        cognizance_second_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='2.不认识']").click()
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
        #62、第二个嫌疑人没有使用交通工具离开现场
        second_no_instructions = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有']").click()
        #64、第二个嫌疑人逃跑路线
        second_escape_route = driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("往商场右拐角处跑了")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        #65、无法对第二个嫌疑人辩认
        no_recognize_second_suspect = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无法辨认']").click()
        # 66、请问嫌疑人是否有留下联系方式
        contact_way = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        # 67、请问现场有无留下痕迹物证
        physical_evidence = driver.find_element_by_xpath("//android.widget.TextView[@text='1.有']").click()
        # 68、物证的特征
        evicence_feature = driver.find_element_by_xpath("//android.widget.EditText[@text='例如：内裤、内衣、精斑等特征']").send_keys("不可明物体")
        confirm_button = driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        # 69、请问嫌疑人有无使用避孕套
        condom = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无']").click()
        # 70、请问嫌疑人是否在体内射精
        internal_cum_shot = driver.find_element_by_xpath("//android.widget.TextView[@text='1.是']").click()
        # 71、请问被强奸后是否在冲凉
        take_a_shower = driver.find_element_by_xpath("//android.widget.TextView[@text='1.是']").click()
        # 72、请问强奸后的内裤能否提供给公安机关
        provide_evidence = driver.find_element_by_xpath("//android.widget.TextView[@text='1.能']").click()
        # 73、请问是否第一时间向公安机关报案
        report_first = driver.find_element_by_xpath("//android.widget.TextView[@text='1.是']").click()
        #86、无监控录像
        surveillance_vide = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无监控录像']").click()
        #87、无可疑线索
        clue = driver.find_element_by_xpath("//android.widget.TextView[@text='2.无可疑线索']").click()
        #88、对报案无补充
        have_add = driver.find_element_by_xpath("//android.widget.TextView[@text='2.没有补充']").click()
        #89、提交
        submit = driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        #90、属实
        true_button = driver.find_element_by_xpath("//android.widget.Button[@text='属实']").click()

        sleep(3)
        driver.quit()
if __name__ == '__main__':
    unittest.main()







