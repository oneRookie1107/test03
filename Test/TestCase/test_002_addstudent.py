import os
import time

import pytest
from selenium import webdriver

from Common.parse_yml import parser_yml
from Test.PageObject.worklist_page import *
from Test.PageObject.addstudent_page import *
from Test.PageObject.login_page import *
import random
from Common.parse_csv import parser_csv
from Config.save_driver_object import DriverObject
from Test.PageObject.studentlist_page import StudentListScenario, StudentListPer,StudentDeletePer

host=parser_yml(os.path.join(os.getcwd(),'Config/redmine.yml'),'websites','host')
add_url=parser_yml(os.path.join(os.getcwd(),'Config/redmine.yml'),'url','student_list_url')
addurl=host+add_url
params=parser_csv(os.path.join(os.getcwd(),r'Data\test_002_addstudent.csv'))
@pytest.mark.parametrize('username,sex,code,phone,fimaly,status,message',params)
class TestAddStudnt():
    def setup_class(self):
        self.driver=DriverObject.driver
        self.add_exist_oper=AddExistOper(self.driver)
        self.driver.get(addurl)#要先跳再刷新，不然刷新的就是首页，而且不会跳对应目标页(因为不等刷新返回来就开始执行下面的代码了，导致了到目标页后又返回了刷新的结果）
    def teardown_class(self):
        #删除已添加的学生
        self.driver.refresh()
        stulist=StudentListScenario(self.driver)
        dele=StudentListPer(self.driver)
        detemi=StudentDeletePer(self.driver)
        for student in params:
            username=student[0]
            status=student[5]
            if status:
                stulist.seartch(username)
                try:
                    dele.click_delete()
                except Exception as e:
                    print('数据没有新增成功{}'.format(username))
                else:
                    detemi.click_delete_determine()
    def test_addstudent(self,username,sex,code,phone,fimaly,status,message):
        self.driver.refresh()#刷新下防止受上一个用例的影响（比如上一个失败了弹窗还在的话不刷新就会影响下一个用例）
        #登录账号
        Addstudent_Scenario(self.driver).addstudent(username,sex,code,phone,fimaly)
        if status=='1':
            assert WebDriverWait(self.driver,5).until(lambda x:message in x.page_source)
        else:
            assert self.add_exist_oper.get_title_content()==message
# if __name__=='__main__':
#     pytest.main(['-vs'])

