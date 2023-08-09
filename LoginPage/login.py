from selenium import webdriver
from rich.console import Console
from rich.theme import Theme
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from UserPage.user import user_allFunctions
from config import sleep_timeout_short, sleep_timeout_long, sleep_timeout_medium

chromeOptions = Options()

custom_theme = Theme({'success': 'green', 'error': 'bold red'})

serv_obj = Service("C:/BrowserDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
console = Console(theme=custom_theme)

driver.get("https://staging.salesta.jp/login")
driver.maximize_window()

# # First time login with login info
# driver.find_element(By.ID, 'login-form_tenantId').send_keys('AriSaf')
# sleep_timeout_short()
# driver.find_element(By.ID, 'login-form_userId').send_keys('300')
# sleep_timeout_short()
# driver.find_element(By.ID, 'login-form_password').send_keys('846882')
# sleep_timeout_short()
# driver.find_element(By.ID, 'loginSubmitButton').click()
# sleep_timeout_long()
# # Set the email
# driver.find_element(By.ID, 'email').send_keys('esrat.arisaftech@gmail.com')
# sleep_timeout_medium()
# driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div/div/div/div/form/div[7]/div/div/div/button').click()
# sleep_timeout_long()
# driver.find_element(By.ID, 'email').send_keys('esrat.arisaftech@gmail.com')
# sleep_timeout_medium()
# driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div/div/div/div/form/div[7]/div/div/div/button').click()
# sleep_timeout_long()
# driver.find_element(By.LINK_TEXT, '登録画面へ戻り、最初からやり直す').click()
# # First time login with login info
# driver.find_element(By.ID, 'login-form_tenantId').send_keys('AriSaf')
# sleep_timeout_short()
# driver.find_element(By.ID, 'login-form_userId').send_keys('300')
# sleep_timeout_short()
# driver.find_element(By.ID, 'login-form_password').send_keys('846882')
# sleep_timeout_short()
# driver.find_element(By.ID, 'loginSubmitButton').click()
# sleep_timeout_long()
# # Set the email
# driver.find_element(By.ID, 'email').send_keys('esrat.arisaftech@gmail.com')
# sleep_timeout_medium()
# driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div/div/div/div/form/div[7]/div/div/div/button').click()
# sleep_timeout_long()
# # Get the OTP
# driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div/div/div/div/form/div[2]/div/div/div/button').click()
# sleep_timeout_medium()
# # Reset password
# driver.find_element(By.ID, 'oldPassword').send_keys('846882')
# sleep_timeout_short()
# driver.find_element(By.ID, 'newPassword').send_keys('password')
# sleep_timeout_short()
# driver.find_element(By.ID, 'newPasswordConfirm').send_keys('password')
# sleep_timeout_short()
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/section/main/div/div/div/div/div/form/div[4]/div/div/div/button').click()
# sleep_timeout_long()
# # Go to login page
# driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div/div/div/div/button').click()
# sleep_timeout_medium()

# Login
driver.find_element(By.ID, 'login-form_tenantId').send_keys('AriSaf')
sleep_timeout_short()
driver.find_element(By.ID, 'login-form_userId').send_keys('1')
sleep_timeout_short()
driver.find_element(By.ID, 'login-form_password').send_keys('password')
sleep_timeout_short()
driver.find_element(By.ID, 'loginSubmitButton').click()
sleep_timeout_long()

try:
    if driver.find_element(By.ID, 'root').is_displayed():
        console.print('Login: Successful ✔', style='success')

        # All User Functions

        try:
            user_allFunctions(driver, "https://staging.salesta.jp")
            console.print('All User Functions: Successful ✔', style='success')
        except Exception as e:
            console.print('All User Functions: Failed! 👎', style='error')
            console.print(f"Error from All User Functions: {e}")


except Exception as e:

    console.print('Login: Failed! 👎', style='error')
    console.print(f"Error from login: {e}")

try:
    if driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[3]/aside/div/ul/li[5]/span').is_displayed():
        console.print('Logout: Successful ✔', style='success')
except Exception as e:
    console.print('Logout: Failed! 👎', style='error')
    console.print(f"Error from logout: {e}")
    driver.close()
