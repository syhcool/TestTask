#-*- coding:utf-8 -*-
#use:syh
from testpro1.zuoye.ui_zuoye.po.add_member_page import AddMemberPage
from testpro1.zuoye.ui_zuoye.po.base_page import BasePage
from testpro1.zuoye.ui_zuoye.po.contact_page import ContactPage


class MainPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_Contact(self):
        """
        进入企业微信首页，点击通讯录页面
        :return:
        """
        return ContactPage(self.driver)
    def goto_add_member(self):
        """
        进入企业微信首页，点击添加成员
        :return:
        """
        self.driver.find_element_by_css_selector(".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)