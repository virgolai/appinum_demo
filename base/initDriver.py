# -*- coding=utf-8 -*-
from appium import webdriver


def initDriver():
    desired_caps = dict()
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "5.1.1"
    desired_caps["deviceName"] = "*****"
    desired_caps["appPackage"] = "com.tpshop.malls"
    desired_caps["appActivity"] = "com.tpshop.malls.SplashActivity"
    desired_caps["resetKeyboard"] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["noReset"] = True # 默认是False，每次都是首次进入
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver

