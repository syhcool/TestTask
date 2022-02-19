#-*- coding:utf-8 -*-
#use:syh

"""
1. 实现页面细节
2. 优化测试用例
3. 封装basepage

"""
from selenium.webdriver.common.by import By

from testpro1.zuoye.ui_zuoye.po.base_page import BasePage



class AddMemberPage(BasePage):
    def add_member(self,name):
        """
        添加成员操作页面
        :return:返回通讯录页面的实例对象
        """
        # 导入操作复制在方法内部，解决循环导入问题
        from testpro1.zuoye.ui_zuoye.po.contact_page import ContactPage
        self.driver.find_element(By.ID,"username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("P0144")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15900000001")
        self.driver.find_element_by_css_selector(".js_btn_save").click()

        return  ContactPage(self.driver)
