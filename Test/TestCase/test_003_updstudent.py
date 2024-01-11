import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Config.save_driver_object import DriverObject
from Test.PageObject.addstudent_page import AddstudentOper,Addstudent_Scenario,AddExistOper
from Common.parse_csv import parser_csv
from Common.parse_yml import parser_yml
from Test.PageObject.studentlist_page import StudentListScenario, StudentListPer, StudentDeletePer
import os
add_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_003_updstudent.csv'),is_dict=1,is_add=1)
upd_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_003_updstudent.csv'),is_dict=0,is_add=0)
delet_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_003_updstudent.csv'),is_dict=1)
host=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'websites','host')
add_url=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'url','student_list_url')
addurl=host+add_url
class TestUpdstudent():
    def setup_class(self):
        self.driver=DriverObject.driver
        self.update_per=AddstudentOper(self.driver)
        self.student_list_per=StudentListPer(self.driver)
        self.student_list_scena=StudentListScenario(self.driver)
        self.exist=AddExistOper(self.driver)
        self.driver.get(addurl)
        self.driver.refresh()#刷新下避免上一个用例影响
        for student in add_data:
            print(add_data)
            Addstudent_Scenario(self.driver).addstudent(student.get('username'))
            time.sleep(1)
            self.driver.refresh()
    def teardown_class(self):
        #删除已添加的学生
        self.driver.refresh()
        detemi=StudentDeletePer(self.driver)
        for student in delet_data:
            username=student['username']
            status=student['status']
            if status:
                print('开始删除数据{}'.format(username))
                self.student_list_scena.seartch(username)
                try:
                    self.student_list_per.click_delete()
                except Exception as e:
                    print('数据没有新增成功{}'.format(username))
                else:
                    detemi.click_delete_determine()
    @pytest.mark.parametrize('username,status,message,is_add,new_name',upd_data)
    def test_updstudent(self,username,status,message,is_add,new_name):
        # self.driver.refresh()
        print('测试更新',username,status,message,is_add,new_name,upd_data)
        self.student_list_scena.seartch(username)
        self.student_list_per.click_update()
        self.update_per.enter_username(new_name)
        self.update_per.click_submit()
        if status==1:
            assert WebDriverWait(self.driver,5).until(lambda x:message in x.page_source)
        else:
            assert message in self.exist.get_title_content()
# if __name__=='__main__':
#     pytest.main(['-vs','test_003_updstudent.py'])

