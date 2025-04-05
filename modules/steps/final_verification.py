from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinalVerificationModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_success(self):
        """Verify if the final success message is shown"""
        try:
            # First attempt with UiAutomator
            try:
                success_element = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("رسید سند حمل بار")'
                )
                if success_element.is_displayed():
                    print("Final verification successful - Found success message using UiAutomator")
                    return True
            except Exception:
                print("Could not verify success with UiAutomator, trying XPath...")
                
                # Second attempt with XPath
                success_element = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="رسید سند حمل بار"]')
                ))
                if success_element.is_displayed():
                    print("Final verification successful - Found success message using XPath")
                    return True
            
            print("Could not find success message")
            return False
            
        except Exception as e:
            print(f"Final verification failed: {str(e)}")
            return False

    def back_to_home(self):
        """Return to the main page"""
        try:
            # First attempt with content-desc
            try:
                home_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="صفحه اصلی"]')
                ))
                home_button.click()
                print("Clicked home button using content-desc")
                return True
            except Exception:
                print("Could not find home button by content-desc, trying text...")
                
                # Second attempt with text
                home_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="صفحه اصلی"]')
                ))
                home_button.click()
                print("Clicked home button using text")
                return True
                
        except Exception as e:
            print(f"Failed to return to home: {str(e)}")
            return False 