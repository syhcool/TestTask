#-*- coding:utf-8 -*-
#use:syh
from selenium.webdriver.common.by import By

from testpro1.zuoye.ui_zuoye.po.add_member_page import AddMemberPage
from testpro1.zuoye.ui_zuoye.po.base_page import BasePage


class ContactPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    def goto_add_member(self):
        """
        通讯录页面,跳转到添加成员页面
        :return:
        """
        while True:
            try:
                self.driver.find_elements_by_css_selector(".js_add_member").click()
                ele = self.driver.find_element(By.ID,"username")
                if ele:
                    break
            except:
                print("元素未能找到")
        return AddMemberPage(self.driver)

    def get_member_list(self):
        """
        获取成员列表
        :return: 返回用于断言的成员列表信息
        """
        elements = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = [name.text for name in elements]
        print(name_list)
        return name_list
