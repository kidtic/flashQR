# flashQR
自动报名抢课（由于qqweb不提供支持了，所以没办法只能用图像方法）

* 此为0.1版，只实现了半自动化。由于qq群图片在消息栏中有遮挡，所以无法识别，需要点开图片才能识别。
* 识别二维码后自动用谷歌浏览器打开网页，之后由于谷歌浏览器可以记录登录状态密码，所以可以直接点报名。
* 未经过实际测试，大概在2秒内可以完成报名。

# step
1. 环境配置:python3 + 需要3个库
    ```
    pip3 install pyzbar
    pip3 install pyautogui
    pip3 install opencv-python
    ```

2. 设置谷歌浏览器路径
    ```text
    #config
    cutRegion_size=1/4 #中间二维码识别区域的尺寸，没必要识别整个屏幕
    chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    ```
3. 打开QQ打开qq群，尽量把消息窗口放在旁边，因为打开图片的窗口在底层。
4. 运行程序`python flashQR.py`,最小化。
5. 等待群发送二维码，发了之后，快速双击二维码，在中间会弹出二维码图片。
6. 会瞬间弹出网页，如果以前登录过的就不用再输密码了，点击报名即可。

*ps.提前打开谷歌浏览器，反应会更快*

# 后续
尽量实现全自动化吧，qq全是坑，就不能用微信吗？？？

如果没想到更好的解决方法就用这个吧。