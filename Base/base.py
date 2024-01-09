import time

from selenium.webdriver.support.wait import WebDriverWait
'''
重新封装了selenium的定位方法，简化locator跟每次都需要写元素查找时间那些,统一了查找时间跟间隔，方便统一管理
'''
class Base():
    def __init__(self,driver):
        self.driver=driver
    #转换by定位方法值
    def split_locator(self,locator):
        '''
        :param locator: 定位方法+定位表达式,str,逗号分隔，前一个是定位方法，后一个是定位表达式
        :return:返回对应转换后的定位方法+定位表达式(主要是转换by值，转成driver.find_element方法可以解析的值）。如果传入的by值不在枚举值中会报错哦
        '''
        by=locator.split(',',maxsplit=1)[0]
        value=locator.split(',',maxsplit=1)[1]
        locator_dict={
            'id':'id',
            'classname':'class name',
            'name':'name',
            'tagname':'tag name',
            'link':'link text',
            'plink':'partial link text',
            'xpath':'xpath',
            'css':'css selector'
        }
        if by not in locator_dict.keys():
            raise NameError('Locator Err! only id,classname,name,tagname,link,plink,xpath,css can be used')
        return locator_dict.get(by),value
    #查找元素
    def wait_find_element(self,locator,sec=20,message='控件找不到'):
        '''
        :param locator:定位方法+定位表达式,str,逗号分隔，前一个是定位方法，后一个是定位表达式
        :param sec: 等待时间，默认20秒
        :return: 返回查找到的元素，找不到会报错
        '''
        time.sleep(0.6)
        try:
            ele=WebDriverWait(self.driver,sec,1).until(lambda x:x.find_element(*self.split_locator(locator)),message)
            return ele
        except Exception as e:
            raise e
    #查找元素集合
    def wait_find_elements(self,locator,sec=20,message='控件集找不到'):
        '''
        :param locator: 定位方法+定位表达式,str,逗号分隔，前一个是定位方法，后一个是定位表达式
        :param sec: 等待秒数，默认20，循环间隔默认是1秒
        :return: 返回查找到的元素集列表，找不到会报错
        '''
        time.sleep(0.6)
        try:
            ele=WebDriverWait(self.driver,sec,1).until(lambda x:x.find_elements(*self.split_locator(locator)),message)
            return ele
        except Exception as e:
            raise e
    def wait_find_text(self,element,sec=3,default_content='',message='2秒内查找不到对应元素内容'):
        def find_content(x):
            if element.text and element.text!=default_content:
                return element.text
        try:
            return WebDriverWait(self.driver,sec,1).until(lambda x:find_content(x),message)
        except Exception as e:
            raise e

