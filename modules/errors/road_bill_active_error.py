# modules/errors/road_bill_active_error.py

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..steps.logout import LogoutModule  # Import the LogoutModule

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
                print("✅ Detected 'Road bill active' error.")
                return True

        except Exception as e:
            print(f"⚠️ No Road Bill Active Error detected: {str(e)}")
        return False

    def click_forward_icon(self):
        """Helper function to click forward icon."""
        try:
            forward_icon = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("")'
            )
            forward_icon.click()
            print("✅ Clicked forward icon using UiAutomator.")
            return True
        except Exception as e:
            print(f"⚠️ UiAutomator forward icon failed: {str(e)}. Trying XPath...")
            try:
                forward_icon_xpath = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@resource-id="iconIcon" and @text=""]'
                )))
                forward_icon_xpath.click()
                print("✅ Clicked forward icon using XPath.")
                return True
            except Exception as ex:
                print(f"❌ Both forward icon methods failed: {str(ex)}")
                return False

    def handle_error(self):
        """Handle the road bill active error by:
        1. Clicking 'متوجه شدم' 
        2. Clicking back icon twice
        3. Clicking forward icon 3 times
        4. Clicking back icon 4 times
        5. Performing logout
        """
        try:
            # 1. First, acknowledge the error
            confirm_button = self.wait.until(EC.presence_of_element_located((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="متوجه شدم"]'
            )))
            confirm_button.click()
            print("✅ Clicked 'متوجه شدم' to acknowledge the error.")
            time.sleep(1)

            # Helper function for back icon clicks
            def click_back_icon():
                try:
                    back_icon = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("").instance(1)'
                    )
                    back_icon.click()
                    print("✅ Clicked back icon using UiAutomator.")
                    return True
                except Exception as e:
                    print(f"⚠️ UiAutomator method failed: {str(e)}. Trying XPath...")
                    try:
                        back_icon_xpath = self.wait.until(EC.presence_of_element_located((
                            AppiumBy.XPATH,
                            '(//android.widget.TextView[@resource-id="iconIcon"])[2]'
                        )))
                        back_icon_xpath.click()
                        print("✅ Clicked back icon using XPath.")
                        return True
                    except Exception as ex:
                        print(f"❌ Both back icon methods failed: {str(ex)}")
                        return False

            # 2. Click back twice
            for _ in range(2):
                if not click_back_icon():
                    return False
                time.sleep(1)

            # 3. Click forward 3 times
            for _ in range(3):
                if not self.click_forward_icon():
                    return False
                time.sleep(1)

            # 4. Click back 4 times
            for _ in range(4):
                if not click_back_icon():
                    return False
                time.sleep(1)

            # 5. Perform logout
            print("⏳ Attempting logout after handling error...")
            logout = LogoutModule(self.driver)
            if not logout.perform_logout():
                print("❌ Failed to logout after handling error")
                return False
            print("✅ Successfully logged out after handling error")

            return True

        except Exception as e:
            print(f"❌ Failed to handle error: {str(e)}")
            return False