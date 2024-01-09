import time

from selenium import webdriver

from Base.base import *
from Test.PageObject.login_page import LoginScenario


class AddstudentPage():
    def __init__(self,driver):
        self.driver=driver
    #新增按钮暂放这里，应该还有个班级管理页面存放这些按钮
    def find_addstudent(self):
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='zt-basic-table-header__toolbar']/button[2]")),'新增学生控件找不到')
        return Base(self.driver).wait_find_element("xpath,//div[@class='zt-basic-table-header__toolbar']/button[2]",message='新增学生控件找不到')
    def find_username(self):
        return Base(self.driver).wait_find_element("xpath,//form[@class='ant-form ant-form-horizontal']/div[1]/div[2]/div/div/input",message='学生姓名控件找不到')
        # return WebDriverWait(self.driver,6).until(EC.presence_of_element_located((By.XPATH,"//form[@class='ant-form ant-form-horizontal']/div[1]/div[2]/div/div/input")),'学生姓名控件找不到')
    def find_sex_female(self):
        return Base(self.driver).wait_find_element("xpath,//input[@class='ant-radio-input' and @value=2]",message='学生性别控件找不到')
        # return WebDriverWait(self.driver,6).until(EC.presence_of_element_located((By.XPATH,"//input[@class='ant-radio-input' and @value=2]")),'学生性别控件找不到')
    def find_code(self):
        return Base(self.driver).wait_find_element("id,form_item_code",message='学号控件找不到')
    def find_phone(self):
        return Base(self.driver).wait_find_element('id,form_item_phoneNo',message='手机号控件找不到')
    def find_relations(self):
        return Base(self.driver).wait_find_elements("xpath,//div[@class='ant-form-item-control-input']//input[contains(@id,'rc_select_')]",message='关系控件找不到')
    def find_relation_datas(self,relation):
        return Base(self.driver).wait_find_elements("xpath,//div[@class='ant-select-item-option-content' and contains(.,'{}')]".format(relation),message='关系{}找不到'.format(relation))
    def find_fimaly_phones(self):
        return Base(self.driver).wait_find_elements("xpath,//input[@placeholder='请输入家长手机号码']",message='家长号码找不到')
    #支持查找第n个x，默认n为1
    def find_fimaly_xes(self):
        return Base(self.driver).wait_find_elements("xpath,//input[@placeholder='请输入家长手机号码']/following-sibling::button",message='家长删除控件找不到')
    def find_add_fimaly(self):
        return Base(self.driver).wait_find_element("xpath,//span[contains(text(),'添加家长')]/..",message='添加家长按钮找不到')
    def find_submit(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='footer-area']/button[2]",message='保存控件找不到')
        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='footer-area']/button[2]")),'保存控件找不到')
    def find_cancel(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='ant-modal-footer']//button[@class='ant-btn']",message='取消控件找不到')
    def find_xes(self):
        return Base(self.driver).wait_find_element("xpath,//button[@class='ant-modal-close']//span[@class='anticon anticon-close']",message='x控件找不到')
    def find_title(self):
        return Base(self.driver).wait_find_element("xpath,//span[@class='zt-basic-title']",message='弹窗标题控件找不到')
class AddExistPop():
    def __init__(self,driver):
        self.driver=driver
    def find_title_content(self):
        return Base(self.driver).wait_find_element("xpath,//span[@class='anticon anticon-close ant-modal-close-icon']/../../following-sibling::div[1]/div",message='新增已存在弹窗标题不存在')
    def find_xes(self):
        return Base(self.driver).wait_find_element("xpath,//span[@class='anticon anticon-close ant-modal-close-icon']",message='新增已存在弹窗的x按钮没找到')
class AddstudentOper():
    def __init__(self,driver):
        self.addstudent_page=AddstudentPage(driver)
        self.js='arguments[0].click()'
        self.driver=driver
    def click_addstudent(self):
        self.driver.execute_script(self.js,self.addstudent_page.find_addstudent())
    def enter_username(self,username):
        self.addstudent_page.find_username().clear()
        self.addstudent_page.find_username().send_keys(username)
    def set_sex_female(self):
        self.driver.execute_script(self.js,self.addstudent_page.find_sex_female())
    def enter_code(self,code):
        self.addstudent_page.find_code().clear()
        self.addstudent_page.find_code().send_keys(code)
    def enter_phone(self,phone):
        self.addstudent_page.find_phone().clear()
        self.addstudent_page.find_phone().send_keys(phone)
    def select_relation(self,relation='妈妈',num=1):
        self.addstudent_page.find_relations()[num-1].click()#点击选择关系弹窗
        self.addstudent_page.find_relation_datas(relation)[num-1].click()#选择关系
        # print('看看能拿到text吗，测试用的',self.addstudent_page.find_relation_datas(relation)[num-1].text)
    def enter_fimaly_phone(self,phone,num=1):
        self.addstudent_page.find_fimaly_phones()[num-1].clear()
        self.addstudent_page.find_fimaly_phones()[num-1].send_keys(phone)
    def click_fimaly_x(self,num=1):
        self.addstudent_page.find_fimaly_xes()[num-1].click()
    def click_add_fimaly(self):
        self.addstudent_page.find_add_fimaly().click()
    def click_submit(self):
        self.driver.execute_script(self.js,self.addstudent_page.find_submit())
    def click_cancel(self):
        self.addstudent_page.find_cancel().click()
    def click_xes(self):
        self.addstudent_page.find_xes().click()
    def get_title_content(self):
        return self.addstudent_page.find_title().text
class AddExistOper():
    def __init__(self,driver):
        self.add_exist_pop=AddExistPop(driver)
    def get_title_content(self):
        return self.add_exist_pop.find_title_content().text
    def click_xes(self):
        return self.add_exist_pop.find_xes().click()
#新增学生页面场景（从点击新增按钮到提交，传入学生姓名跟性别，性别默认男，传值为2时会切换成女）
class Addstudent_Scenario():
    def __init__(self,driver):
        self.addstudent_oper=AddstudentOper(driver)
    def addstudent(self,student_name,sex='男',code='',phone='',fimalys=[]):
        '''
        :param student_name: 学生姓名，必填
        :param sex: 性别，1为男2为女，默认1
        :param code: 学号，默认空
        :param phone: 手机号，默认空
        :param fimalys: 家长信息，默认[],格式[[关系,手机号],[关系2,手机号2]]
        :return: None
        '''
        self.addstudent_oper.click_addstudent()
        self.addstudent_oper.enter_username(student_name)
        if code:
            self.addstudent_oper.enter_code(code)
        if sex=='女':
            self.addstudent_oper.set_sex_female()
        if phone:
            self.addstudent_oper.enter_phone(phone)
        fimaly_num=len(fimalys)
        if fimaly_num>0:
            num=1
            for fimaly in fimalys:
                if num>1:
                    self.addstudent_oper.click_add_fimaly()#点击新增家长
                self.addstudent_oper.select_relation(fimaly[0],num)
                self.addstudent_oper.enter_fimaly_phone(fimaly[1],num)
                num+=1
        self.addstudent_oper.click_submit()
        # time.sleep(3)#为啥没有这个等待就没有保存？？？？-点了保存后太快刷新页面了ajax还没请求上..

if __name__=='__main__':
    print('测试用')
    opt=webdriver.ChromeOptions()
    prefs={'download.default_directory':'D:\\下载数据存放\\'}#配置浏览器下载数据存放路径
        # prefs['profile.managed_default_content_settings.images']=2#1配置不加载图片
        # prefs['permissions.default.stylesheet']=2#2配置不加载css,值设置0就是加载（目前没看到啥效果）
    opt.add_experimental_option('detach',True)#设置浏览器不会自动关闭
    opt.add_experimental_option('prefs',prefs)
    opt.add_argument('--start-maximized')# 最大化运行（全屏窗口）
    url="https://oauat.gzhtedu.cn/timemeow/#/login"
    driver=webdriver.Chrome(options=opt)
    driver.set_page_load_timeout(60)
    driver.get(url)
    LoginScenario(driver).login('cszoaxx0000','abc@123456')#登录
    #进入学生列表页
    print('开始跳别的页面')
    # driver.get('http://www.baidu.com')
    driver.get('https://oauat.gzhtedu.cn/timemeow/#/bureauSchoolMange/schoolManage/studentManage?branchId=687007746105257985&gradeId=687010485765255169&classId=687020304879038464&orgId=687007744616280064&gradeClassName=%E4%B8%80%E5%B9%B4%E7%BA%A74%E7%8F%AD&isGraduate=0')
    stu=Addstudent_Scenario(driver)
    # stu.addstudent('xue99',2,'809','15677789098',[['妈妈','15677790000'],['爸爸','15677881111'],['爷爷','15344462222']])
    # stu.addstudent('xue100')
    add=Addstudent_Oper(driver)
    add.click_addstudent()
    print(add.get_title_content())
    time.sleep(2)
    # add.click_xes()
    # add.click_addstudent()
    # time.sleep(2)
    # print('选择妈妈啦')
    # add.select_relation()
    # print('点击新增学生')
    # add.click_add_fimaly()
    # # time.sleep(5)
    # add.select_relation('爸爸',2)
    # add.enter_username('xue236')
    # print('选择性别')
    # add.set_sex_female()
    # print('输入学号')
    # add.enter_code(6890)
    # print('输入号码')
    # add.enter_fimaly_phone('15644461012')
    # add.enter_fimaly_phone('15744461012',2)
    # print('再点击新增家长')
    # add.click_add_fimaly()
    # print('删除一个家长')
    # add.click_x(3)
    # print('输入手机号')
    # add.enter_phone(15844461012)
    # print('点击提交')
    # # add.click_submit()
    time.sleep(6)
    driver.quit()
