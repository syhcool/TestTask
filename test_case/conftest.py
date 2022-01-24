# encoding = utf-8
import pytest
import logging


@pytest.fixture()
def login():
    print('开始计算')
    yield "token"
    print('计算结束')


