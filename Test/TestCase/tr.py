import os
import time
from selenium import webdriver
# opt=webdriver.ChromeOptions()
# prefs={'download.default_directory':'D:\\下载数据存放\\'}#配置浏览器下载数据存放路径
# opt.add_experimental_option('detach',True)#设置浏览器不会自动关闭
# opt.add_experimental_option('prefs',prefs)
# opt.add_argument('--start-maximized')# 最大化运行（全屏窗口）
# # opt.add_argument('headless')#无界面运行
# driver=webdriver.Chrome(options=opt)
# driver.set_page_load_timeout(30)
# driver.get('https://k12.gzhtedu.cn/#/login')
from Common.parse_csv import parser_csv

print('自动化用例啦')
def test_git():
    print('测试呢啥玩意改名字啦')
    assert True
# time.sleep(5)
# driver.quit()
print('地址呢',os.getcwd(),parser_csv(os.path.join(os.getcwd(),'Data/test_001_login.csv')))
