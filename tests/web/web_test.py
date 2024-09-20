import pytest
from tests.web.test_base import WebBase
from tests.web.pages.calculator_page import CalculatorPage
from tests.web.pages.login_page import LoginPage
from tests.web.pages.register_page import RegisterPage
import assertpy
from random import randint
class TestWeb(WebBase):




    def test_login(self):
        LoginPage(self.driver).login('admin','test1234')
        assert CalculatorPage(self.driver).elements.username.text == 'admin'
        CalculatorPage(self.driver).elements.logout.click()
    

    def test_register(self):
        name = "eiad" + str(randint(1,200))
        LoginPage(self.driver).elements.register.click()
        RegisterPage(self.driver).do_register(name,'123456')
        username_text = CalculatorPage(self.driver).elements.username.get_attribute(name)
        assert username_text == name
        CalculatorPage(self.driver).elements.logout.click()


    def test_add(self):
        LoginPage(self.driver).login('admin','test1234')
        assert CalculatorPage(self.driver).add(1,2) == 3
        CalculatorPage(self.driver).elements.logout.click()


    def test_sub(self):
        LoginPage(self.driver).login('admin','test1234')
        assert CalculatorPage(self.driver).sub(6,2) == 4
        CalculatorPage(self.driver).elements.logout.click()

    def test_mul(self):
        LoginPage(self.driver).login('admin','test1234')
        assert CalculatorPage(self.driver).mul(2,2) == 4
        CalculatorPage(self.driver).elements.logout.click()

    def test_divide(self):
        LoginPage(self.driver).login('admin','test1234')
        assert CalculatorPage(self.driver).divide(6,2) == 3
        CalculatorPage(self.driver).elements.logout.click() 

    def test_history(self):
        LoginPage(self.driver).login('admin','test1234')
        CalculatorPage(self.driver).add(1,2)
        assert CalculatorPage(self.driver).history_text() == '1+2=3\n'
        CalculatorPage(self.driver).elements.clear_history.click()
        assert CalculatorPage(self.driver).history_text() == ''
        CalculatorPage(self.driver).elements.logout.click()