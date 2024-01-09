import time


import pytest
import os
from Config.save_driver_object import DriverObject
from Test.PageObject.studentlist_page import StudentListPer
from Common.parse_yml import parser_yml
host=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'websites','host')
add_url=parser_yml(os.path.join(os.getcwd(),r'Config/redmine.yml'),'url','student_list_url')
student_list=host+add_url
class TestPaging():
    def setup_class(self):
        self.driver=DriverObject.driver
        self.student_list_per=StudentListPer(self.driver)
        self.driver.get(student_list)
    def test_paging(self):
        self.driver.refresh()
        print('执行自动化用例啦')
        # time.sleep(1)
        self.student_list_per.click_next_page()#这里会拿到旧的定位数据？？？--具体原因不太清楚，后面了解前端后再看看
        assert self.student_list_per.get_numpage_backgroud_color_hex(1)=='#f4f4f5' and self.student_list_per.get_numpage_backgroud_color_hex(2)=='#1989fa'
        try:
            self.student_list_per.click_previous_page()
            assert self.student_list_per.get_numpage_backgroud_color_hex(2)=='#f4f4f5' and self.student_list_per.get_numpage_backgroud_color_hex(1)=='#1989fa'
        except Exception as e:
            assert False
# if __name__=='__main__':
#     pytest.main(['-vs','test_006_paging.py'])

