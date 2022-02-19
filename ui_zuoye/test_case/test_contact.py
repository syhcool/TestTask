#-*- coding:utf-8 -*-
#use:syh
from testpro1.zuoye.ui_zuoye.po.contact_page import ContactPage


class TestContact:
    def test_contact(self):
        contact = ContactPage()
        contact.goto_add_member()