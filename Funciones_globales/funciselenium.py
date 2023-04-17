import time
import unittest
import random
from selenium import webdriver
import pywinauto
from selenium.webdriver.common.keys import Keys
from pywinauto import application
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class Funciones_Globales():

    def __init__(self,driver):
        self.driver=driver

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t

    def Navegar(self, Url,Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: "+str(Url))
        t = time.sleep(Tiempo)
        return t

    def Texto_Mixto(self,tipo,selector,texto,tiempo):
        if(tipo=="xpath"):
            i = 1 
            while i ==1:
                try:
                    val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                    val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                    val = self.driver.find_element(By.XPATH, selector)
                    val.clear()
                    val.send_keys(texto)
                    print("Escribiendo en el campo {} el texto -> {} ".format(selector,texto))
                    t = time.sleep(tiempo)
                    return t
                    i= 0
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Elemento" + selector)
                    return t
                except ElementClickInterceptedException as ex:
                    print("No se encontro el Campo {}  ".format(selector))
        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Click_Mixto(self, tipo, selector,tiempo):
        if (tipo == "xpath"):
            i = 1
            a = 0
            while i == 1:
                try:
                    val = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
                    t = time.sleep(tiempo)
                    val.click()
                    return t
                    i = 0
                    print(i)
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Campo {}  ".format(selector))
                except ElementClickInterceptedException as ex:
                    print("No se encontro el Campo {}  ".format(selector))
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                val.click()
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t


    def Click_NotScroll(self, selector, tiempo):
            i = 1
            a = 0
            while i == 1:
                try:
                    val = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
                    t = time.sleep(tiempo)
                    val.click()
                    return t
                    i = 0
                    print(i)
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Campo {}  ".format(selector))
                except ElementClickInterceptedException as ex:
                    print("No se encontro el Campo {}  ".format(selector))
                
    def Click_selects(self, selector):
            try:
                val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                  

    def End(self):
        print("**Se termina el flujo de compras correctamente**")


    def Upload_Xpath(self, xpath,ruta):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            # t = time.sleep(tiempo)
            # return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            # return t

    #Funciòn Radio y Check
    def Check_Xpath(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_xpath(xpath)
            val.click()
            print("Click en el elemento {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t

    def Check_ID(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            val.click()
            print("Click en el elemento {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    def Check_Xpath_Multiples(self, tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(num)
                val.click()
                print("Click en el elemento {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el Elemento" + num)

    def Comment_text(self,selector,texto):
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.click()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector,texto))

    def xpath_buttons(self, xpath):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                val = self.driver.find_element(By.XPATH, xpath)
                val.click()
            except TimeoutException as ex:
                print(ex.msg)
                print(" No se encontro " + xpath)

    def optionmultiselect(self,xpath):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                ActionChains(self.driver).click(val).send_keys(Keys.ESCAPE).perform()
            except TimeoutException as ex:
                print(ex.msg)
                print(" No se encontro " + xpath)

    def uploadfile(self, name_file):
            app = application.Application().connect(path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            mainWindow = app['Abrir'] # main windows' title
            ctrl=mainWindow['Edit']
            mainWindow.SetFocus()
            ctrl.ClickInput()
            ctrl.TypeKeys(name_file)
            ctrlBis = mainWindow['Abrir'] # open file button
            ctrlBis.ClickInput()
           
    def Textkeyenenter(self, selector):
        searchprov = self.driver.find_element(By.XPATH, selector)
        ActionChains(self.driver).click(searchprov).send_keys( Keys.ENTER,"prueba1",Keys.ARROW_DOWN, Keys.ENTER).perform()

    def gettext(self, selector):
        val1 = self.driver.find_element(By.XPATH, selector)
        val2 = val1.get_attribute('value')
        print(val2)

    def sendkeys(self,selector, tiempo, text):
            i = 1
            while i == 1:
                try:
                    val = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
                    val = self.driver.find_element(By.XPATH, selector)
                    val.send_keys(text, Keys.ENTER)
                    t = time.sleep(tiempo)
                    return t
                    i = 0
                    print(i)
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Campo {}  ".format(selector))
                except ElementClickInterceptedException as ex:
                    print("No se encontro el Campo {}  ".format(selector))


    def alertascarga(self):
        pass
    #exista
    #intercepte
        