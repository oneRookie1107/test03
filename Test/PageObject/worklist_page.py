# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from Base.base import *
class WorklistPage():
    def __init__(self,driver):
        self.driver=driver
    def find_work(self):
        return Base(self.driver).wait_find_element("xpath,//button[@class='ant-btn zt-layout-nav-selected']",message="工作台控件找不到")
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='ant-btn zt-layout-nav-selected']")),'工作台控件找不到')
    def find_schoolset(self):
        return Base(self.driver).wait_find_element("xpath,//li[@class='zt-menu-submenu zt-simple-menu__parent']",message="学校设置控件找不到")
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//li[@class='zt-menu-submenu zt-simple-menu__parent']")),'学校设置控件找不到')
    def find_classset(self):
        return Base(self.driver).wait_find_element("xpath,//li[@class='zt-menu-item zt-simple-menu__children']",message="班级列表控件找不到")
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//li[@class='zt-menu-item zt-simple-menu__children']")),'班级列表控件找不到')
    def find_classmanage(self):
        return Base(self.driver).wait_find_element("xpath,//button[@class='ant-btn ant-btn-link btn'][1]",message="班级管理表控件找不到")
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='ant-btn ant-btn-link btn'][1]")),'班级管理表控件找不到')
class WorklistOper():
    def __init__(self,driver):
        self.worklist_page=WorklistPage(driver)
        self.driver=driver
        self.js='arguments[0].click()'
    def click_work(self):
        self.driver.execute_script(self.js,self.worklist_page.find_work())#通过js点击工作台按钮
    #后面的待完成
    def click_schoolset(self):
        self.driver.execute_script(self.js,self.worklist_page.find_schoolset())
    def click_classset(self):
        self.driver.execute_script(self.js,self.worklist_page.find_classset())
    def click_classmanage(self):
        self.driver.execute_script(self.js,self.worklist_page.find_classmanage())
class WorklistScenario():
    def __init__(self,driver):
        self.worklist_oper=WorklistOper(driver)
    #进入学生管理
    def enter_studentlist(self):
        self.worklist_oper.click_work()
        self.worklist_oper.click_schoolset()
        self.worklist_oper.click_classset()
        self.worklist_oper.click_classmanage()


