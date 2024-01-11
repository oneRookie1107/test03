import csv,json
def parser_csv(file_path,is_dict=0,**kwargs):
    '''
    :param file_path:str,文件绝对地址
    :param is_dict:int，是否返回字典，默认0，0话会返回[[],[]]，内容为从第二行开始的表内容。非0会返回列表嵌字典，字典的键为表格第一行，值为表格第二行开始的内容
    :param kwargs：过滤条件（不传为返回所有内容），传入键值对，键为表头，值为表格第二行开始的内容
    :return: [[],[]] or [{},{}],返回过滤后的文件内容（去除首行表头）
    '''
    with open(file_path,'r',encoding='utf-8') as f:
        fs=csv.DictReader(f)
        result=[]
        for values in fs:
            values=dict(values)
            is_fiflter=1
            #过滤数据
            for key,valu in kwargs.items():
                if values.get(key) is None or str(values.get(key))!=str(valu):
                    is_fiflter=0
                    break
            #将数据里的非字符串转成python中数据
            for key,value in values.items():
                try:
                    values[key]=eval(value)
                except Exception as e:
                    pass
            #根据入参返回不同数据格式
            if is_fiflter and is_dict:
                result.append(values)
            elif is_fiflter and is_dict==0:
                result.append(list(values.values()))
        return result
# print(parser_csv(r'D:\pythondir\uoframework\Data\test_003_updstudent.csv',is_dict=1))
