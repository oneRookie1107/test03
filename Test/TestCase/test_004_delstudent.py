import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Config.save_driver_object import DriverObject
from Test.PageObject.studentlist_page import StudentListScenario,StudentDeletePer,StudentListPer
from Test.PageObject.addstudent_page import Addstudent_Scenario
from Common.parse_csv import parser_csv
add_data=parser_csv(r'D:\pythondir\uoframework\Data\test_004_delstudent.csv',is_dict=1,is_add=1)
del_data=parser_csv(r'D:\pythondir\uoframework\Data\test_004_delstudent.csv',is_dict=0,is_add=0)
student_list_url=r'https://k12.gzhtedu.cn/#/bureauSchoolMange/schoolManage/studentManage?branchId=688838369647562752&gradeId=775417402929242112&classId=775417404158115842&orgId=688838369102303232&gradeClassName=%E5%B0%8F%E7%8F%AD2%E7%8F%AD&isGraduate=0'
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
