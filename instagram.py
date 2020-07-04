from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


import time
import pickle

class Instagram:
    __loggedIn = False
    def __init__(self,usrname,curpwd):
        """ Constructor that takes username and password as argument,
            loads the instagram main page of that particular id"""

        self.__usrname = usrname
        self.__curpwd = curpwd
        

    def logIn(self):
        self.__loggedIn = True
        self.driver = webdriver.Safari() 
        self.driver.delete_all_cookies()
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()

        time.sleep(2)

        loginField = self.driver.find_element_by_xpath('//input[@name = "username"]')
        loginField.send_keys(self.__usrname)
        passwordField = self.driver.find_element_by_xpath('//input[@name = "password"]')
        passwordField.send_keys(self.__curpwd)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()

        time.sleep(4)

        try:
            noConnectionMessage = self.driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
            if noConnectionMessage.isDisplayed() == True :
                print("NO INTERNET CONNECTION")
        except NoSuchElementException:
            print('ERROR CAUGHT')
        self.driver.find_element_by_xpath('//button[contains(text(),"Not Now")]').click()
        time.sleep(10)

    
    def changePassword(self,newpwd):
        if self.__loggedIn == False:
            self.logIn()
 
        self.driver.find_element_by_xpath("//a[contains(text(),'" + self.__usrname +"')]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//button[contains(text(),"Edit Profile")]').click()   
        time.sleep(4)    
        self.driver.find_element_by_xpath('//a[contains(text(),"Change Password")]').click()
        
        time.sleep(4)
        oldpasswordField = self.driver.find_element_by_xpath('//input[@name = "cppOldPassword"]')
        oldpasswordField.send_keys(self.__curpwd)
        time.sleep(2)
        newpasswordField = self.driver.find_element_by_xpath('//input[@name = "cppNewPassword"]')
        newpasswordField.send_keys(newpwd)
        time.sleep(2)
        confirmpasswordField = self.driver.find_element_by_xpath('//input[@name = "cppConfirmPassword"]')
        confirmpasswordField.send_keys(newpwd)
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(),"Change Password")]').click()  
        time.sleep(4)   
        file = open("PasswordFile.p","wb")
        file.seek(0)
        file.truncate
        pickle.dump(newpwd,file)
        file.close()
        return newpwd
        

    def Username(self):
        return self.__usrname


    def Password(self):
        return pickle.load(open("PasswordFile.p","rb"))


    def close(self):
        if self.__loggedIn == True:
             self.driver.close()  
        
    




