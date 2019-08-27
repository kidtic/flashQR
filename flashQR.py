# 0.1 版本说明：
# 半自动模式。因为刚开始qq窗口刷出来的图片下方有名字和下载图标遮挡，
# 所以暂时使用手工点开图片的方式来快速扫描二维码并且打开图片


from pyzbar.pyzbar import decode
import pyautogui as gui
import cv2
import numpy as np
import warnings
import webbrowser

#忽略警告错误
warnings.filterwarnings("ignore")
#config
cutRegion_size=1/4 #中间二维码识别区域的尺寸，没必要识别整个屏幕
chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

if __name__ == '__main__':
    #获得屏幕尺寸
    screen_size=gui.screenshot().size
    print(screen_size)
    #0.1版本暂时只截取中间点出来的二维码
    cutRegion=(screen_size[0]/2-screen_size[0]*cutRegion_size/2,
               screen_size[1]/2-screen_size[0]*cutRegion_size/2,
               screen_size[0]*cutRegion_size,
               screen_size[0]*cutRegion_size)
    i=0
    while(1):

        #截屏识别二维码
        img=np.array(gui.screenshot(region=cutRegion))
        img=cv2.resize(img,(512,512))
        decode_str=decode(img)
        if len(decode_str)>=1:
            url=decode_str[0].data.decode("utf-8")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open(url, new=1, autoraise=True)
            print(url)
            break



