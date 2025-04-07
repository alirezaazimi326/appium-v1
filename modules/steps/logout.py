from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogoutModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def perform_logout(self):
        """Perform the logout process"""
        try:
            # Click on menu button (trying different locator strategies)
            try:
                # Try first locator
                menu_button = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH, 
                    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]'
                )))
            except Exception:
                try:
                    # Try second locator
                    menu_button = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.ViewGroup").instance(11)'
                    )
                except Exception:
                    # Try third locator
                    menu_button = self.wait.until(EC.presence_of_element_located((
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc=""]'
                    )))
            
            menu_button.click()
            print("Clicked on menu button")
            time.sleep(1)

            # Click on settings button (trying different locator strategies)
            try:
                # Try first locator
                settings_button = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("تنظیمات")'
                )
            except Exception:
                try:
                    # Try second locator
                    settings_button = self.wait.until(EC.presence_of_element_located((
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="تنظیمات"]'
                    )))
                except Exception:
                    # Try third locator
                    settings_button = self.wait.until(EC.presence_of_element_located((
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[contains(@content-desc, "تنظیمات")]'
                    )))

            settings_button.click()
            print("Clicked on settings button")
            time.sleep(1)

            # Click on profile button (trying different locator strategies)
            try:
                # Try first locator
                profile_button = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup'
                )))
            except Exception:
                # Try second locator
                profile_button = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@resource-id="iconIcon" and @text=""]'
                )))

            profile_button.click()
            print("Clicked on profile button")
            time.sleep(1)

            # Click on logout button (trying different locator strategies)
            try:
                # Try first locator
                logout_button = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="خروج از حساب"]'
                )))
            except Exception:
                # Try second locator
                logout_button = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("خروج از حساب")'
                )

            logout_button.click()
            print("Clicked on logout button")
            time.sleep(1)

            return True

        except Exception as e:
            print(f"Error during logout: {str(e)}")
            return False 