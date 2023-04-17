import time
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones_globales.funciselenium import Funciones_Globales

t = 1

class Login_qasoul(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver
        
    def loginqa(self):
        #Se realiza llamado de funciones globales
        f = Funciones_Globales(self.driver)
        #Se realiza llamado de funciones globales
        f.Texto_Mixto("xpath", "//input[@id='mat-input-0']", "funcionario.mer",t)
        f.Texto_Mixto("xpath", "//input[@id='mat-input-1']", "Montechelo2022*", t)
        f.Click_Mixto("xpath", "//button[@type='submit']", t)
        sleep(6)

    def menucompras(self):
        #Se realiza llamado de funciones globales
        f = Funciones_Globales(self.driver)
        #Se entra al modulo de comercial
        f.Click_Mixto("xpath", "(//div[contains(.,'Menú')])[3]", t)
        f.Click_Mixto("xpath", "//button[contains(.,'Módulos')]", t)
        f.Click_Mixto("xpath", "//button[contains(.,'Mercadeo')]", t)


