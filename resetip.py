#不同的路由器可能id不一样
#这是大部分通用的
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://192.168.1.1")
print("浏览器已打开，正在访问路由器页面...")

try:

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_username"))
    )
    print("已找到用户名输入框")


    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_password"))
    )
    print("已找到密码输入框")


    username.send_keys("useradmin")
    password.send_keys("sdddddc")
    print("已输入用户名和密码")


    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
    )
    submit_button.click()
    print("已点击登录按钮")


    restart_menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "menu_action_restart_hint"))
    )
    restart_menu_button.click()
    print("已点击重启菜单按钮")


    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[1]"))
    )
    confirm_button.click()
    print("已点击确认重启按钮，路由器正在重启...")


    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "some_element_after_reboot")))
    print("路由器重启成功")

except TimeoutException as e:
    print(f"操作超时: {e}")

finally:
    driver.quit()
    print("浏览器已关闭")
