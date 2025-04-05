from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Step7PaymentModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self):
        """Verify if we're on step 7 by checking the title"""
        try:
            # First attempt with UiAutomator
            try:
                title_element = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("کرایه و صدور سند حمل")'
                )
                if title_element.is_displayed():
                    print("Step 7 verification successful - Found title using UiAutomator")
                    return True
            except Exception:
                print("Could not verify title with UiAutomator, trying XPath...")
                
                # Second attempt with XPath
                title_element = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="کرایه و صدور سند حمل"]')
                ))
                if title_element.is_displayed():
                    print("Step 7 verification successful - Found title using XPath")
                    return True
            return False
        except Exception as e:
            print(f"Step 7 verification failed: {str(e)}")
            return False

    def click_continue(self):
        """Click on the continue button"""
        try:
            # First attempt with UiAutomator description
            try:
                continue_button = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("ادامه")'
                )
                continue_button.click()
                print("Clicked continue button using UiAutomator description")
                return True
            except Exception:
                print("Could not find continue button by UiAutomator description, trying content-desc...")
                
                # Second attempt with content-desc
                try:
                    continue_button = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
                    ))
                    continue_button.click()
                    print("Clicked continue button using content-desc")
                    return True
                except Exception:
                    print("Could not find continue button by content-desc, trying text...")
                    
                    # Third attempt with text
                    continue_button = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.TextView[@text="ادامه"]')
                    ))
                    continue_button.click()
                    print("Clicked continue button using text")
                    return True
        except Exception as e:
            print(f"Failed to click continue button: {str(e)}")
            return False

    def verify_and_continue(self):
        """Complete payment verification process"""
        try:
            if self.verify_step_title():
                time.sleep(0.5)  # Wait for animations
                if not self.click_continue():
                    return False
                return True
            return False
        except Exception as e:
            print(f"Step 7 payment verification failed: {str(e)}")
            return False 