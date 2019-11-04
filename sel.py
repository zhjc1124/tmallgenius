import os
import pyttsx
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from playsound import playsound
username = 'zhjc1124@gmail.com' # 你的淘宝账号
password = 'Qwerty7620' # 你的淘宝密码
starttime = '09:30' # 每天的启动时间

# 设置参数
options = ChromeOptions()

# headless模式无法运行
# options.add_argument('--headless')

# 不加载图片,加快访问速度
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# 设置为开发者模式，避免被识别
options.add_experimental_option('excludeSwitches',
                                ['enable-automation'])

# 打开页面
driver = Chrome(executable_path="./chrome/chromedriver.exe", options=options)
wait = WebDriverWait(driver, 40)

driver.get('https://login.taobao.com/member/login.jhtml')
try:
    # 这里设置等待：等待输入框
    login_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
    login_element.click()

    sina_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
    sina_login.click()

    weibo_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
    weibo_user.send_keys(username)

    sina_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
    sina_password.send_keys(password)

    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
    submit.click()

    taobao_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                             '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
    # 登陆成功打印提示信息
    print(f"登陆成功：{taobao_name.text}")
    driver.get('http://tb.cn/DL1Ouwv')

    # 获取每日指令
    cmd_xpath = '//*[@id="root"]/div/div[3]/div[1]/div[3]/div[2]/div[1]/span[2]'
    cmd = wait.until(EC.presence_of_element_located((By.XPATH, cmd_xpath))).text
    print(f"获取到今日指令为{cmd}")
    
    engine = pyttsx.init()
    engine.say(cmd)
    engine.runAndWait()
except Exception:
    driver.close()
    print("登陆失败")







