import pytest
from selenium import webdriver
from Common.parse_yml import parser_yml
from Test.PageObject.login_page import LoginScenario

host=parser_yml('D:/pythondir/uoframework/Config/redmine.yml','websites','host')
login_url=parser_yml('D:/pythondir/uoframework/Config/redmine.yml','url','login_url')
homeurl=host+login_url
username=parser_yml('D:/pythondir/uoframework/Config/redmine.yml','user','username')
pwd=parser_yml('D:/pythondir/uoframework/Config/redmine.yml','user','pwd')
from Config.save_driver_object import DriverObject
@pytest.fixture(scope='session',autouse=True)
def login_fixture():
    opt=webdriver.ChromeOptions()
    prefs={'download.default_directory':'D:\\下载数据存放\\'}#配置浏览器下载数据存放路径
    opt.add_experimental_option('detach',True)#设置浏览器不会自动关闭
    opt.add_experimental_option('prefs',prefs)
    opt.add_argument('--start-maximized')# 最大化运行（全屏窗口）
    driver=webdriver.Chrome(options=opt)
    driver.set_page_load_timeout(60)
    driver.get(homeurl)
    # driver.get('http://www.baidu.com')
    LoginScenario(driver).login(username,pwd)
    DriverObject.driver=driver
    yield driver
    driver.quit()
