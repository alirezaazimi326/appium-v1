from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Step5UnloadingModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self):
        """Verify if we're on step 5 by checking the title"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="محل تخلیه بار ..."]')
            ))
            if title_element.is_displayed():
                print("Step 5 verification successful - Found unloading location title")
                return True
            return False
        except Exception as e:
            print(f"Step 5 verification failed: {str(e)}")
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
                print("Could not find location selector by resource-id, trying full path...")
                
                # Second attempt with full path
                try:
                    location_selector = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]')
                    ))
                    location_selector.click()
                    print("Selected location using full path")
                    return True
                except Exception:
                    print("Could not find location selector by full path, trying UiAutomator...")
                    
                    # Third attempt with UiAutomator
                    location_selector = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.ViewGroup").instance(20)'
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
            # First attempt with content-desc
            try:
                confirm_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="تأیید مقصد"]')
                ))
                confirm_button.click()
                print("Clicked confirm button using content-desc")
                return True
            except Exception:
                print("Could not find confirm button by content-desc, trying UiAutomator...")
                
                # Second attempt with UiAutomator
                confirm_button = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("تأیید مقصد")'
                )
                confirm_button.click()
                print("Clicked confirm button using UiAutomator")
                return True
        except Exception as e:
            print(f"Failed to click confirm button: {str(e)}")
            return False

    def select_unloading_location(self):
        """Complete unloading location selection process"""
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
            print(f"Step 5 unloading location selection failed: {str(e)}")
            return False 