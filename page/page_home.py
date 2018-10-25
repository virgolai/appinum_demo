# -*- coding=utf-8 -*-
import time
from selenium.webdriver.common.by import By
from base.baseaction import Baseaction


class HomePageAction(Baseaction):
    # 定义 home页面动作需要使用到的元素特征 button
    # into_btn_feature = By.ID,"com.tpshop.malls:id/start_Button"
    home_btn_feature = By.XPATH,( "text,首页,1","resource-id,com.tpshop.malls:id/tab_txtv,1" )

    # 给 home 模型定义了一个动作，可以实现自动进入首页的操作
    def auto_enter_home(self):

        # 通过强制等待让加载界面消失
        time.sleep( 3 )

        try:
            self.find_element(self.home_btn_feature)
            print( "欢迎使用TPShop，进入主界面" )
        except Exception:
            # 执行三次滑屏操作 【因此这个操作具有通用性，所以我们选择将它放置于Base当中】
            for i in range(3):
                self.swipe_left()
                time.sleep(2)
        self.driver.

