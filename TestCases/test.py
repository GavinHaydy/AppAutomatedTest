from appium import webdriver
import unittest
from Page.calculator import Browser


class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities={
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.miui.calculator',
            'appActivity': '.cal.CalculatorActivity'
        })

    def test_case(self,):
        page = Browser(self.driver)
        page.agree()
        page.one()
        page.add()
        page.nine()
        page.equ()

    def tearDown(self) -> None:
        pass
