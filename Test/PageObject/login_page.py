# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from Base.base import *
#页面元素对象层（返回对应对象或者对象属性）
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    def find_username(self):
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'form_item_username')),'用户名控件找不到')
        return Base(self.driver).wait_find_element("id,form_item_username",message='用户名控件找不到')
    def find_pwd(self):
        return Base(self.driver).wait_find_element("id,form_item_password",message='密码控件找不到')
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'form_item_password')),'密码控件找不到')
    def find_login(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='zt-login-pane']/button",message='登录按钮控件找不到')
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='zt-login-pane']/button")),'密码控件找不到')
    def find_shoolname(self):
        return Base(self.driver).wait_find_element("xpath,//span[@class='zt-header-user-dropdown__name truncate']",message='登录后的学校名控件找不到')
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='zt-header-user-dropdown__name truncate']")),'登录后的学校名控件找不到')
#页面元素操作层
class LoginOper():
    def __init__(self,driver):
        self.login_page=LoginPage(driver)
        self.js='arguments[0].click()'
        self.driver=driver
    def input_username(self,username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)
    def input_pwd(self,pwd):
        self.login_page.find_pwd().clear()
        self.login_page.find_pwd().send_keys(pwd)
    def click_login(self):
        self.driver.execute_script(self.js,self.login_page.find_login())#通过js点击登录按钮
    def get_schoolname(self):
        return self.login_page.find_shoolname().text#返回登录成功的学校名
#定义基本场景
class LoginScenario():
    def __init__(self,driver):
        self.page_oper=LoginOper(driver)
    def login(self,username,pwd):
        self.page_oper.input_username(username)
        self.page_oper.input_pwd(pwd)
        self.page_oper.click_login()
        self.page_oper.get_schoolname()#加这句是因为登录的时候还没登录完就没有loading了，确保这个场景作为前置场景时是登录成功才跳别的页面，否则别的页面跳转会有问题）
