from Base.base import *
class ClassListPage():
    def __init__(self,driver):
        self.driver=driver
    def find_classmanage(self):
        return Base(self.driver).wait_find_element("xpath,//button[@class='ant-btn ant-btn-link btn'][1]",message="班级管理表控件找不到")
class ClassListPer():
    def __init__(self,driver):
        self.classlist_pae=ClassListPage(driver)
    def click_classmanage(self):
        self.classlist_pae.find_classmanage().click()
