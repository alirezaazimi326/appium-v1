from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Step4LoadingModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self):
        """Verify if we're on step 4 by checking the title"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="محل بارگیری ..."]')
            ))
            if title_element.is_displayed():
                print("Step 4 verification successful - Found loading location title")
                return True
            return False
        except Exception as e:
            print(f"Step 4 verification failed: {str(e)}")
            return False

    def click_location_selector(self):
        """Click on the location selector"""
        try:
            # First attempt with resource-id and text
            try:
                location_selector = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="iconIcon" and @text="󰋚"]')
                ))
                location_selector.click()
                print("Selected location using resource-id and text")
                return True
            except Exception:
                print("Could not find location selector by resource-id, trying UiAutomator...")
                
                # Second attempt with UiAutomator
                location_selector = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.ViewGroup").instance(17)'
                )
                location_selector.click()
                print("Selected location using UiAutomator")
                return True
        except Exception as e:
            print(f"Failed to click location selector: {str(e)}")
            return False

    def click_confirm(self):
        """Click on the confirm button"""
        try:
            confirm_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="تأیید مبدأ"]')
            ))
            confirm_button.click()
            print("Clicked confirm button")
            return True
        except Exception as e:
            print(f"Failed to click confirm button: {str(e)}")
            return False

    def select_loading_location(self):
        """Complete loading location selection process"""
        try:
            if self.verify_step_title():
                time.sleep(1)  # Wait for animations
                if not self.click_location_selector():
                    return False
                time.sleep(1)  # Wait for animations
                if not self.click_confirm():
                    return False
                return True
            return False
        except Exception as e:
            print(f"Step 4 loading location selection failed: {str(e)}")
            return False 