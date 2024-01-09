import time
from selenium import webdriver
from Test.PageObject.login_page import *
#上面的测试用
from Base.base import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
class StudentListPage():
    def __init__(self,driver):
        self.driver=driver
    def find_addstudent(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='zt-basic-table-header__toolbar']/button[2]",message='新增学生控件找不到')
    def find_updates(self):
        return Base(self.driver).wait_find_elements("xpath,//button[@class='ant-btn ant-btn-link btn']",message='修改控件找不到')
    def find_deletes(self):
        return Base(self.driver).wait_find_elements("xpath,//button[@class='ant-btn ant-btn-link ant-btn-dangerous btn']",message='删除控件找不到')
    def find_sertch_studentname(self):
        return Base(self.driver).wait_find_element("id,form_item_userName",message='查找不到学生姓名搜索框')
    def find_sertch_sex(self):
        # try:
            # print('选择了男女后')
            # return Base(self.driver).wait_find_element("xpath,//div[@class='ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow']/div/span[@class='ant-select-selection-item']",message='查找不到性别搜索框')
        # except Exception as e:
        return Base(self.driver).wait_find_element("id,form_item_gender",message='查找不到性别搜索框')#待完成定位有问题？？？？？---选择了性别后性别的点击事件被别的span拦截了，所以这里目前需要在选择性别前刷新页面，这样就永远都是第一次选性别了
    def find_select_sex(self,sex='男'):
        return Base(self.driver).wait_find_element("xpath,//div[contains(@id,'form_item_gender_list') and @role='option' and @aria-label='{}']".format(sex),message='选择的性别{}查找不到'.format(sex))
    def find_search(self):
        return Base(self.driver).wait_find_element("xpath,//button[@class='ant-btn ant-btn-primary']",message='查找不到搜索按钮')
    def find_next_page(self):
        return Base(self.driver).wait_find_element("xpath,//li[@class='ant-pagination-next']",message='查找不到下一页按钮')
    def find_previous_page(self):
        return Base(self.driver).wait_find_element("xpath,//li[@class='ant-pagination-prev']",message='查找不到上一页按钮')
    def find_numpage(self,num=1):
        return Base(self.driver).wait_find_element("xpath,//li[@title={}]".format(num),message='查找不到第{}页'.format(num))
    #因为第一个tr是表头，所以下面用了个num+1
    def find_num_data(self,num=1):
        return Base(self.driver).wait_find_element("xpath,//tbody[@class='ant-table-tbody']/tr[{}]".format(int(num)+1),message='查找不到第{}条数据'.format(num))
    def find_num_data_attribute(self,num=1,attributenum=1):
        if attributenum%2==1:
            return Base(self.driver).wait_find_element("xpath,//tbody[@class='ant-table-tbody']/tr[{}]/td[{}]/span".format(int(num)+1,attributenum),message='查找不到第{}条数据的第{}个属性'.format(num,attributenum))
        else:
            return Base(self.driver).wait_find_element("xpath,//tbody[@class='ant-table-tbody']/tr[{}]/td[{}]".format(int(num)+1,attributenum),message='02查找不到第{}条数据的第{}个属性'.format(num,attributenum))
    def find_no_data(self):
        return Base(self.driver).wait_find_element("xpath,//p[@class='ant-empty-description']",message='暂无数据控件找不到')
class StudentDeletePrompt():
    def __init__(self,driver):
        self.driver=driver
    def find_delete_pop(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='ant-modal-content']",message='删除弹窗找不到')
    def find_delete_determine(self):
        return Base(self.driver).wait_find_element("xpath,//button[@class='ant-btn ant-btn-primary ant-btn-dangerous ant-btn-error']",message='删除弹窗的确定按钮找不到')
    def find_delete_cancellation(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='footer-area']/button[@class='ant-btn']",message='删除弹窗的取消按钮找不到')
    def find_delete_x(self):
        return Base(self.driver).wait_find_element("xpath,//span[@class='anticon anticon-close']",message='删除弹窗上的x按钮找不到')
    def find_delete_title(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='modal-content']/h2",message='删除弹窗上标题找不到')
    def find_delete_content(self):
        return Base(self.driver).wait_find_element("xpath,//div[@class='modal-content']/p",message='删除弹窗上内容找不到')

class StudentListPer():
    def __init__(self,driver):
        self.student_list_page=StudentListPage(driver)
        self.driver=driver
        self.js='arguments[0].click()'
    def click_addstudent(self):
        self.student_list_page.find_addstudent().click()
    #点击修改按钮，默认点击第一条数据的修改
    def click_update(self,num=1):
        # print('拿到修改按钮',self.student_list_page.find_updates()[num-1])
        self.driver.execute_script(self.js,self.student_list_page.find_updates()[num-1])
    def click_delete(self,num=1):
        # self.student_list_page.find_deletes()[num-1].click()
        self.driver.execute_script(self.js,self.student_list_page.find_deletes()[num-1])
    def enter_seartch_stuname(self,stuname):
        self.student_list_page.find_sertch_studentname().clear()
        self.student_list_page.find_sertch_studentname().send_keys(stuname)
    def click_seartch_sex(self):
        self.student_list_page.find_sertch_sex().click()
    #选择性别通过键盘实现，对应性别元素是div无法通过点击实现
    def select_male(self):
        self.student_list_page.find_sertch_sex().send_keys(Keys.ENTER)
    def select_female(self):
        self.student_list_page.find_sertch_sex().send_keys(Keys.ARROW_DOWN)
        self.student_list_page.find_sertch_sex().send_keys(Keys.ENTER)
    def click_seartch(self):
        self.student_list_page.find_search().click()
    #页码的已测试
    def click_next_page(self):
        self.student_list_page.find_next_page().click()
    def click_previous_page(self):
        self.student_list_page.find_previous_page().click()
    def click_numpage(self,num):
        self.student_list_page.find_numpage(num).click()
    def get_numpage_backgroud_color_hex(self,num):
        return Color.from_string(self.student_list_page.find_numpage(num).value_of_css_property('background-color')).hex
    #通过获取第一条数据判断列表是否渲染完毕,下面的测试完毕
    def page_rederinged(self):
        self.student_list_page.find_num_data()
    def get_data_stuname(self,num=1):
        return self.student_list_page.find_num_data_attribute(num,1).text
    def get_data_studentId(self,num=1):
        return self.student_list_page.find_num_data_attribute(num,2).text
    def get_data_stusex(self,num=1):
        return self.student_list_page.find_num_data_attribute(num,3).text
    def get_nodata_context(self):
        return self.student_list_page.find_no_data().text
class StudentDeletePer():
    def __init__(self,driver):
        self.student_delete_prompt=StudentDeletePrompt(driver)
        self.driver=driver
    def click_delete_determine(self):
        self.student_delete_prompt.find_delete_determine().click()
    def click_delete_cancellation(self):
        self.student_delete_prompt.find_delete_cancellation().click()
    def click_delete_x(self):
        self.student_delete_prompt.find_delete_x().click()
    def get_delete_title(self):
        # return self.student_delete_prompt.find_delete_title().text
        return Base(self.driver).wait_find_text(self.student_delete_prompt.find_delete_title())
    def get_delete_content(self):
        # return self.student_delete_prompt.find_delete_content().text
        return Base(self.driver).wait_find_text(self.student_delete_prompt.find_delete_content())
    def get_del_pop(self):
        return self.student_delete_prompt.find_delete_pop()
class StudentListScenario():
    def __init__(self,driver):
        self.student_list_per=StudentListPer(driver)
    #搜索场景封装
    def seartch(self,stuname='',sex=''):
        self.student_list_per.enter_seartch_stuname(stuname)
        if sex=='男':
            print('性别男')
            self.student_list_per.click_seartch_sex()
            self.student_list_per.select_male()
        elif sex=='女':
            print('性别女')
            self.student_list_per.click_seartch_sex()
            self.student_list_per.select_female()
        elif sex:
            raise NameError('输入的性别有误，仅支持男、女')
        self.student_list_per.page_rederinged()#确认列表渲染完毕后再点击搜索，否则开始渲染出来的数据会覆盖搜索结果
        # time.sleep(2)#多次搜索不加等待还是有问题，在删除上一次搜索内容时会加载无条件的内容，然后搜索的时候容易把无条件的结果渲染回来
        self.student_list_per.click_seartch()
        return self.student_list_per.page_rederinged()
class StudentDeleteScenario():
    def __init__(self,driver):
        self.student_delete_per=StudentDeletePer(driver)
    def student_delete(self,num=1):
        pass
        #暂时不需要封装的

if __name__=="__main__":
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
    # stu=StudentListScenario(driver)
    # print('开始搜索')
    # stu.seartch('邱韵婷')
    # print('搜索完毕')
    # print(stu.student_list_per.get_data_studentId(),stu.student_list_per.get_data_stuname())
    # time.sleep(2)
    # print('点击下一页')
    stu=StudentListPer(driver)
    dele=StudentDeletePer(driver)
    # stu.click_next_page()
    # time.sleep(2)
    # print('刷新啦')
    # driver.refresh()
    # time.sleep(5)
    # print()
    # time.sleep(2)
    # print('点击上一页')
    # stu.click_previous_page()
    # time.sleep(2)
    print('点击第三页啦')
    stu.click_numpage(3)
    # print('点击删除啦1')
    # time.sleep(2)#
    stu.click_delete(1)
    print('打印弹窗内容',dele.get_delete_content(),dele.get_delete_title())
    print('点击取消')
    dele.click_delete_cancellation()
    print('点击删除啦2')
    stu.click_delete(2)
    print('打印弹窗内容',dele.get_delete_content(),dele.get_delete_title())
    # time.sleep(2)#
    print('点击x')
    dele.click_delete_x()
    # time.sleep(2)#
    print('点击删除啦3')
    stu.click_delete(3)
    print('打印弹窗内容',dele.get_delete_content(),dele.get_delete_title())
    print('点击确定')
    dele.click_delete_determine()
    print('点击删除啦4')
    time.sleep(2)#点确定的时候调ajax了，不加个等待会拿到上一页的元素后面点删除删除弹窗都出不来
    stu.click_delete(4)
    print('打印弹窗内容',dele.get_delete_content(),dele.get_delete_title())
    time.sleep(6)
    driver.quit()
