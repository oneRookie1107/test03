import pytest
from selenium import webdriver
from Test.PageObject.login_page import *
from Common.parse_csv import parser_csv
from Common.parse_yml import parser_yml
# param=[['cszoaxx0000','abc@12345',0,''],['cszoaxx0000','abc@123456',1,'测试组OA学校']]
param=parser_csv('D:/pythondir/uoframework/Data/test_001_login.csv')
host=parser_yml('D:/pythondir/uoframework/Config/redmine.yml','websites','host')
homeurl=host+'/ztoe/index.html#/login'
def asserttips(x):
    return '用户或密码不正确' in x.page_source
class TestLogin():
    def setup_method(self):
        opt=webdriver.ChromeOptions()
        prefs={'download.default_directory':'D:\\下载数据存放\\'}#配置浏览器下载数据存放路径
        # prefs['profile.managed_default_content_settings.images']=2#1配置不加载图片
        # prefs['permissions.default.stylesheet']=2#2配置不加载css,值设置0就是加载（目前没看到啥效果）
        opt.add_experimental_option('detach',True)#设置浏览器不会自动关闭
        opt.add_experimental_option('prefs',prefs)
        opt.add_argument('--start-maximized')# 最大化运行（全屏窗口）
        url=homeurl
        self.driver=webdriver.Chrome(options=opt)
        self.driver.set_page_load_timeout(60)
        self.driver.get(url)
    def teardown_method(self):
        self.driver.quit()
    @pytest.mark.parametrize(('username','pwd','status','schoolname'),param)
    def test_login(self,username,pwd,status,schoolname):
        LoginScenario(self.driver).login(username,pwd)
        if status=='1':
            print('判断登录成功')
            assert LoginOper(self.driver).get_schoolname()==schoolname
        elif status=='0':
            print('判断登录失败')
            assert  WebDriverWait(self.driver,5).until(asserttips) and self.driver.current_url==homeurl
        else:
            print('status参数值不对，值只能为1或0')
# if __name__=='__main__':
#     pytest.main(['-vs','--collect-only'])    #这个都不生效了

#待调试
