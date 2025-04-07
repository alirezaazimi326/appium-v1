from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BeforeLoginModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_continue(self):
        """Click on the initial continue button before login"""
        try:
            continue_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
            ))
            print("Found Continue button, clicking it...")
            continue_button.click()
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Continue button not found: {str(e)}")

            # Check if already on login screen
            try:
                login_element = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("ورود یا ثبت نام جدید")'
                )))
                print("Already on login screen.")
                return True
            except Exception as login_check_error:
                print(f"Login screen not detected either: {str(login_check_error)}")
                return False
