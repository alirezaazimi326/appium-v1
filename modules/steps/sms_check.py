from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

class SmsCheckModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def check_sms_prompt(self):
        """Check if SMS verification prompt is present"""
        try:
            # Try first locator
            try:
                sms_text = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("لطفا پیامک دریافت شده را اینجا وارد نمایید")'
                )
            except Exception:
                # Try second locator
                sms_text = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="لطفا پیامک دریافت شده را اینجا وارد نمایید"]'
                )))
            
            if sms_text.is_displayed():
                print("\n!!! SMS VERIFICATION DETECTED !!!")
                print("The site is now sending SMS verification")
                print("Stopping all processes...")
                
                # Force quit the driver and Python process
                try:
                    self.driver.quit()
                except:
                    pass
                    
                # Exit the program
                sys.exit("Program terminated due to SMS verification requirement")
                
            return True
            
        except Exception:
            return False 