#-*- coding:utf-8 -*-
#use:syh

'''公共方法'''
from selenium import webdriver


class BasePage:
    _url = " "
    def __init__(self,base_driver = None):
        if base_driver is None:
            option = webdriver.ChromeOptions()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self._url)
            self.driver.implicitly_wait(5)
        else:
            # 将self.driver 添加一个WebDriver对象注解， 解决类型提示的问题
            # 注解本身没有任何的赋值作用，方便IDE 操作
            self.driver:webdriver = base_driver
    def find(self, by, loc=None):
        if loc is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=loc)

    def finds(self, by, loc=None):
        if loc is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by, value=loc)

    def click(self, by, loc=None):
        self.find(by, loc).click()

    def send(self, by, text, loc=None):
        self.find(by, loc).send_keys(text)
