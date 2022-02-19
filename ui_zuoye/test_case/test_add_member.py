#-*- coding:utf-8 -*-
#use:syh
import pytest

from testpro1.zuoye.ui_zuoye.po.main_page import MainPage


class TestAddMember:
    @pytest.mark.parametrize("name",["皮城"])
    def test_add_member(self,name):
        """
        1、跳转到添加用户操作页面后进行的操作
        2、点击保存后跳转到通讯录
        3、获取通讯录信息然后断言
        :return:
        """
        main_page = MainPage()

        assert name in main_page.goto_add_member().add_member(name).get_member_list()