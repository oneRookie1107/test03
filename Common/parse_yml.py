import yaml
def parser_yml(file_path,section='',key=''):
    with open(file_path,'r',encoding='utf-8') as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        if section:
            data=data.get(section)
        if key:
            data=data.get(key)
        return data



