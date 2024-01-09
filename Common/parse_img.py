from PIL import Image
import pytesseract
def parse_img(path,has_chi=True):
    '''
    :param path: str文件绝对路径
    :param has_chi: boolen是否有中文（默认True）
    :return: 返回识别到的图片中的内容
    注意：要使用这个功能必须先安装tesseract软件，并且将安装目录加入到path里面
    '''
    img=Image.open(path)
    img=img.convert('L')#转成灰色
    img=img.convert('1')#转成二进制
    #imag.show()#打开图片查看
    if has_chi:
        return pytesseract.image_to_string(img,lang='chi_sim')
    return pytesseract.image_to_string(img)
if __name__=='__main__':
    text=parse_img(r'D:\cs\down2.jpg')
    print(text)
