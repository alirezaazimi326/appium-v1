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
            print(f"Error clicking continue button: {str(e)}")
            return False 