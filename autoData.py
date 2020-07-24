from appium import webdriver#导入appium包

#连接手机app初始化的一些信息
desc={}

desc['deviceName']='127.0.0.1:62001'#手机设备名称，adb devices
desc['platformVersion']='4.4.2'#手机版本，在手机中：设置--关于手机
desc['platformName']='Android' #手机类型，ios或android
#输入命令，获取app信息：aapt dump badging C:\Users\83473\Desktop\mobileqq_android.apk
desc['appPackage']='com.tencent.mobileqq'#包名
desc['appActivity']='com.tencent.mobileqq.activity.SplashActivity'#启动入口
desc["unicodeKeyboard"] = "True"#appium提供的一种输入法，可以传中文。测试时直接用这个输入法
desc["resetKeyboard"] = "True"#程序结束时重置原来的输入法
desc["noReset"] = "True"#不初始化手机app信息（类似不清楚缓存）


#启动服务端，再cmd窗口输入appium.如果appium没有安装好，可以打开appium-desktop.也相当于启动了服务

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desc)#访问服务接口，并启动手机app。url参数是当appium启动后，默认访问服务地址和接口