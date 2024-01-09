import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Common.parse_yml import parser_yml
from Config.save_driver_object import DriverObject
from Test.PageObject.studentlist_page import StudentListScenario,StudentDeletePer,StudentListPer
from Test.PageObject.addstudent_page import Addstudent_Scenario
from Common.parse_csv import parser_csv
import os
add_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_004_delstudent.csv'),is_dict=1,is_add=1)
del_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_004_delstudent.csv'),is_dict=0,is_add=0)
host=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'websites','host')
student_list_url=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'url','student_list_url')
class TestdelStudent():
    def setup_class(self):
        self.driver=DriverObject.driver
        self.student_list_per=StudentListPer(self.driver)
        self.student_del_per=StudentDeletePer(self.driver)
        self.student_list_scenario=StudentListScenario(self.driver)
        self.driver.get(student_list_url)
        for student in add_data:
            Addstudent_Scenario(self.driver).addstudent(student.get('username'))
        time.sleep(1)
    @pytest.mark.parametrize('username,message,is_add,status,button',del_data)
    def test_del_student(self,username,message,is_add,status,button):
        self.driver.refresh()
        self.student_list_scenario.seartch(username)
        self.student_list_per.click_delete()
        if button=='取消':
            self.student_del_per.click_delete_cancellation()
        elif button=='x':
            self.student_del_per.click_delete_x()
        else:
            self.student_del_per.click_delete_determine()
        if status=='1':
            assert WebDriverWait(self.driver,3).until(lambda x:message in x.page_source)
        assert WebDriverWait(self.driver,2).until(lambda x:self.student_del_per.get_del_pop().is_displayed()==False)
# if __name__=='__main__':
#     pytest.main(['-vs','test_004_delstudent.py'])
