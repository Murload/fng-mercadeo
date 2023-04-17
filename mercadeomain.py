import unittest
from os import remove
from selenium import webdriver
from time import sleep
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Funciones_globales.funciselenium import Funciones_Globales
from Funciones_globales.loginfng import Login_qasoul


class mercadeo(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        # self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver1.exe")
        funciones = Funciones_Globales(self.driver)
        funciones.Navegar("https://fng-qa.mysoul.software/login", 1)
        
    def test_completes(self):
        f = Funciones_Globales(self.driver)
        login = Login_qasoul(self.driver)
        login.loginqa()
        login.menucompras()
        
    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.close()

# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='reportComercial2'))

