# encoding = utf-8
import pytest
import yaml
import logging
import allure

with open("../testyaml/testcase.yaml", 'r', encoding ="utf-8") as f:
    datas = yaml.safe_load(f)["add"]
    cases = datas['case']
    titles = datas['title']

logging.basicConfig(level=logging.INFO)
logging = logging.getLogger()

@allure.feature("测试计算器")
@allure.title("测试相加:{a}+{b}={expect}")
@pytest.mark.parametrize("a,b,expect",cases,ids=titles)
def test_add(login,a,b,expect):
    with allure.step(f'测试{a}+{b}={expect}'):
       assert expect == a + b
       logging.info(f'案例：测试相加:{a}+{b}={expect}执行成功')