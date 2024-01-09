import time

import pytest

from Test.PageObject.addstudent_page import Addstudent_Scenario
from Test.PageObject.studentlist_page import StudentListScenario, StudentListPer, StudentDeletePer
from Config.save_driver_object import DriverObject
from Common.parse_csv import parser_csv
from Common.parse_yml import parser_yml
import os
add_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_005_student_search.csv'),is_dict=1,is_add=1)
search_data=parser_csv(os.path.join(os.getcwd(),r'Data\test_005_student_search.csv'),is_dict=0,is_add=0)
host=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'websites','host')
student_list_url=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'url','student_list_url')
class TestStudentSearch():
    def setup_class(self):
        self.driver=DriverObject.driver
        # self.add_student_scenario=Addstudent_Scenario(self.driver)
        self.student_list_scenario=StudentListScenario(self.driver)
        self.student_list_per=StudentListPer(self.driver)
        self.driver.get(student_list_url)
        for student in add_data:
            Addstudent_Scenario(self.driver).addstudent(student.get('username'),student.get('sex'))
            time.sleep(1)
            self.driver.refresh()
    def teardown_class(self):
        detemi=StudentDeletePer(self.driver)
        for student in add_data:
            self.student_list_scenario.seartch(student.get('username'))
            try:
                self.student_list_per.click_delete()
                detemi.click_delete_determine()
            except Exception as e:
                print('学生-{}-没添加成功'.format(student.get('username')))
            time.sleep(1)
            self.driver.refresh()

    @pytest.mark.parametrize('username,sex,is_add,status,level,message',search_data)
    def test_student_search(self,username,sex,is_add,status,level,message):
        self.student_list_scenario.seartch(username,sex)
        print('搜成功没',username,sex)
        if status=='1':
            if username:
                assert username in self.student_list_per.get_data_stuname()
            if sex:
                assert sex==self.student_list_per.get_data_stusex()
        else:
            assert message in self.student_list_per.get_nodata_context()
        self.driver.refresh()

# if __name__=='__main__':
#     pytest.main(['-vs','test_005_sechstudent.py'])






