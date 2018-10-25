# -*- coding=utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Baseaction:

    def __init__(self,abc):
        self.driver = abc

    # 自定义一个元素查找方法
    def find_element(self, feature):
        #feature = By.XPATH,"//*[@text='显示']"
        print(feature)
        """
        依据用户传入的元素信息特征，然后返回当前用户想要查找元素
        :param feature: 元组类型，包含用户希望的查找方式，及该方式对应的值
        :return: 返回当前用户查找的元素
        """
        by = feature[0]
        value = feature[1]
        wait = WebDriverWait(self.driver, 5, 1)
        print(self.make_xpath(value))
        if by == By.XPATH:
            #print( "说明了用户想要使用 xpath 路径的方式来获取元素" )
            return wait.until(lambda x: x.find_element(by, self.make_xpath(value)))
        else:
            return wait.until(lambda x: x.find_element(feature[0], feature[1]))

    def find_elements(self,feature):
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))

    # 自定义一个元素点击的方法【 这个方法无论是在当前页面还是其它页面都通用 】
    def click(self, feature):
        """
        依据用户传入的元素特征 对其实现点击的操作
        :param feature: 元素的信息元组
        :return:none
        """
        self.find_element(feature).click()

    # 自定义一个函数实现对具体元素进行值的输入
    def input_txt(self, feature, value):
        """
        依据用户传入的元素特征，找到对应的元素，然后在它里面输入我们的传入的 value值
        :param feature: 元组类型，表示元素的特征
        :param value:  用户在元素中输入的内容
        :return: none
        """
        self.find_element(feature).send_keys(value)

    # 自定义了一个可以自动帮我们拼接 xpath 路径的工具函数
    def make_xpath(self,feature):
        start_path = "//*["
        end_path = "]"
        res_path = ""

        if isinstance(feature, str):

            # 如果是字符串 我们不能直接上来就拆我们可以判断一下它是否是默认正确的 xpath 写法
            if feature.startswith("//*["):
                return feature

            # 如果用户输入的是字符串，那么我们就拆成列表再次进行判断
            split_list = feature.split(",")
            if len(split_list) == 2:
                # //*[contains(@text,'设')]
                res_path = "%scontains(@%s,'%s')%s" % (start_path, split_list[0], split_list[1], end_path)
            elif len(split_list) == 3:
                # //[@text='设置']
                res_path = "%s@%s='%s'%s" % (start_path, split_list[0], split_list[1], end_path)
            else:
                print("请按规则使用")
        elif isinstance(feature, tuple):
            for item in feature:
                # 默认用户在元组当中定义的数据都是字符串
                split_list2 = item.split(',')
                if len(split_list2) == 2:
                    res_path += "contains(@%s,'%s') and " % (split_list2[0], split_list2[1])
                elif len(split_list2) == 3:
                    res_path += "@%s='%s' and " % (split_list2[0], split_list2[1])
                else:
                    print("请按规则使用")
            andIndex = res_path.rfind(" and")
            res_path = res_path[0:andIndex]
            res_path = start_path + res_path + end_path
        else:
            print("请按规则使用")

        return res_path

    # 自定义一个获取当前设备尺寸的功能
    def get_device_size(self):
        w = self.driver.get_window_size()["width"]
        h = self.driver.get_window_size()["height"]
        return w,h

    # 自定义一个功能，可以实现向左滑屏操作。
    def swipe_left(self):
        start_x = self.get_device_size()[0]*0.9
        start_y = self.get_device_size()[1]*0.5
        end_x = self.get_device_size()[0]*0.2
        end_y = self.get_device_size()[1]*0.5
        self.driver.swipe( start_x,start_y,end_x,end_y )


























