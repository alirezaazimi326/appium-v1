from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Step6PostalCodeModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_layout(self):
        """Verify if we're on step 6 by checking the layout"""
        try:
            # First attempt with UiAutomator
            try:
                layout = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.ViewGroup").instance(14)'
                )
                if layout.is_displayed():
                    print("Step 6 layout verification successful - Found using UiAutomator")
                    return True
            except Exception:
                print("Could not verify layout with UiAutomator, trying XPath...")
                
                # Second attempt with full XPath
                layout = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
                ))
                if layout.is_displayed():
                    print("Step 6 layout verification successful - Found using XPath")
                    return True
            return False
        except Exception as e:
            print(f"Step 6 layout verification failed: {str(e)}")
            return False

    def verify_postal_code_labels(self):
        """Verify if postal code labels are present"""
        try:
            # Check for source postal code label
            try:
                source_label = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="کد پستی مبدأ : "]')
                ))
                if source_label.is_displayed():
                    print("Found source postal code label")
                    return True
            except Exception:
                print("Could not find source postal code label, trying destination...")
                
                # Check for destination postal code label
                dest_label = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="کد پستی مقصد : "]')
                ))
                if dest_label.is_displayed():
                    print("Found destination postal code label")
                    return True
            return False
        except Exception as e:
            print(f"Postal code label verification failed: {str(e)}")
            return False

    def click_continue(self):
        """Click on the continue button"""
        try:
            # First attempt with content-desc
            try:
                continue_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
                ))
                continue_button.click()
                print("Clicked continue button using content-desc")
                return True
            except Exception:
                print("Could not find continue button by content-desc, trying text...")
                
                # Second attempt with text
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
        """Complete postal code verification process"""
        try:
            if self.verify_step_layout():
                time.sleep(1)  # Wait for animations
                if not self.verify_postal_code_labels():
                    return False
                time.sleep(1)  # Wait for animations
                if not self.click_continue():
                    return False
                return True
            return False
        except Exception as e:
            print(f"Step 6 postal code verification failed: {str(e)}")
            return False 