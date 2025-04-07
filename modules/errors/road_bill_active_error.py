# modules/errors/road_bill_active_error.py

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RoadBillActiveErrorHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_error_present(self):
        """Check if the specific road bill active error popup is present."""
        try:
            error_title = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("خطا")'
            )))

            error_message = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("خودرو شما در حال حاضر دارای بارنامه جاده ای فعال بوده")'
            )))

            if error_title.is_displayed() and error_message.is_displayed():
                print("Detected 'Road bill active' error.")
                return True

        except Exception as e:
            print(f"No Road Bill Active Error detected: {str(e)}")
        return False

    def handle_error(self):
        """Handle the road bill active error by clicking 'متوجه شدم'."""
        try:
            acknowledgment = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("متوجه شدم")'
            )))
            acknowledgment.click()
            print("Clicked 'متوجه شدم' to acknowledge the error.")
            return True

        except Exception as e:
            print(f"Failed to click 'متوجه شدم': {str(e)}")
            return False
