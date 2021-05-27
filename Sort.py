from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class SortBot:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome(r'c:/Users/thayl/Desktop/Thayllon/py/chromedriver.exe')
        self.username = username
        self.password = password

    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com/')

        time.sleep(5)
        browser.find_element_by_name("username").send_keys(self.username)
        time.sleep(1)
        browser.find_element_by_name("password").send_keys(self.password)
        time.sleep(1)
        browser.find_element_by_name("password").send_keys(Keys.RETURN)

        time.sleep(5)

        newnames = self.getFollow()
        self.coment(newnames)

    def getFollow(self):
        browser = self.browser
        browser.get("https://www.instagram.com/{0}/".format(self.username))
        time.sleep(2)
        browser.find_element_by_xpath("//a[@href = '/{0}/followers/']".format(self.username)).click()#Seguidores

        time.sleep(5)
        eula = browser.find_element_by_class_name('isgrP')
        for i in range(5):
            time.sleep(3)
            browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', eula)
        bb = browser.find_element_by_class_name('jSC57')
        time.sleep(1)

        mat = bb.find_elements_by_xpath('//a')
        time.sleep(2)
        names = [elem.get_attribute('title') for elem in mat]

        newnames = []

        for x in names:

            if "" != x:
                newnames.append(x)

        print(newnames)

        return newnames

    def coment(self, newnames):
        browser = self.browser
        browser.get("https://www.instagram.com/p/BjKnxufHgcd/")
        time.sleep(1)



        for i in newnames:
            time.sleep(5)
            browser.find_element_by_class_name("Ypffh").click()
            time.sleep(5)
            browser.find_element_by_class_name("Ypffh").send_keys("@")
            for p in i:
                browser.find_element_by_class_name("Ypffh").send_keys(p)
                time.sleep(random.randint(1,5)/30)
            time.sleep(5)
            browser.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(2)

sort1 = SortBot("----", "----")
sort1.login()
