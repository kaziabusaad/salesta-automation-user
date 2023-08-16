import time
from selenium.webdriver.common.by import By
from config import sleep_timeout_long, sleep_timeout_dwnld
from config import sleep_timeout_short
from config import sleep_timeout_medium
from config import sleep_timeout_long1
from config import sleep_timeout_long
from config import sleep_timeout_longTime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = Options()


def user_allFunctions(driver, url):
    # driver.get(url)
    sleep_timeout_long1()

    # User Home
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[5]/button').click()
        sleep_timeout_long()
        print('User Home: Successful ✔')
    except Exception as e:
        print('User Home: Failed! 👎')
        print(f"Error from User Home: {e}")

    # User Info
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[3]/aside/div/ul/li[2]/span').click()
        sleep_timeout_long()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div/div[3]/div[1]/form/div[3]/'
                                      'div[2]/div/div/span/span/a/button').click()
        sleep_timeout_medium()
        driver.find_element(By.XPATH, '//*[@id="email-change"]/div[4]/div/div/div/button').click()
        sleep_timeout_medium()
        driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[3]/div[1]/form/div[3]/'
                                     'div[2]/div/div/span/span/a/button').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'email-change_email').send_keys('kazi.arisaftech@gmail.com')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'email-change_confirmEmail').send_keys('kazi.arisaftech@gmail.com')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'submitButton').click()
        time.sleep(30)
        driver.find_element(By.ID, 'submitEmailConfirmButton').click()
        sleep_timeout_long()
        # driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/button/span/span/svg').click()
        # sleep_timeout_long()
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button')))
        element.click()
        sleep_timeout_long()
        print('Change Email: Successful ✔')
    except Exception as e:
        print('Change Email: Failed! 👎')
        print(f"Error from Change Email: {e}")

    # Manual
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[3]/aside/div/ul/li[3]/span').click()
        sleep_timeout_long()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div/div/div[2]/button[1]').click()
        sleep_timeout_long()
        print('User Manual: Successful ✔')
    except Exception as e:
        print('User Manual: Failed! 👎')
        print(f"Error from User Manual: {e}")

    # Change Password
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[3]/aside/div/ul/li[4]/span[2]').click()
        sleep_timeout_medium()
        element = driver.find_element(By.ID, 'changePasswordSubmitButton')
        driver.execute_script("arguments[0].click();", element)
        sleep_timeout_medium()
        driver.find_element(By.ID, 'oldPassword').send_keys('password')
        sleep_timeout_short()
        driver.find_element(By.ID, 'newPassword').send_keys('password')
        sleep_timeout_short()
        driver.find_element(By.ID, 'newPasswordConfirm').send_keys('password')
        sleep_timeout_medium()
        # driver.find_element(By.ID, 'oldPassword').send_keys('password')
        # sleep_timeout_short()
        element = driver.find_element(By.ID, 'changePasswordSubmitButton')
        driver.execute_script("arguments[0].click();", element)
        sleep_timeout_long()
        driver.find_element(By.CLASS_NAME, 'ResetPasswordConfirmationComponent_submitButton__y3YUU').click()
        sleep_timeout_long()
        driver.find_element(By.ID, 'login-form_tenantId').send_keys('AriSaf')
        sleep_timeout_short()
        driver.find_element(By.ID, 'login-form_userId').send_keys('1')
        sleep_timeout_short()
        driver.find_element(By.ID, 'login-form_password').send_keys('password')
        sleep_timeout_long()
        driver.find_element(By.ID, 'loginSubmitButton').click()
        sleep_timeout_long()
        print('Change Password: Successful ✔')
    except Exception as e:
        print('Change Password: Failed! 👎')
        print(f"Error from Change Password: {e}")









