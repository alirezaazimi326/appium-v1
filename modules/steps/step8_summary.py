from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Step8SummaryModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self):
        """Verify if we're on step 8 by checking the title"""
        try:
            # First attempt with XPath
            try:
                title_element = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="خلاصه مشخصات سند حمل"]')
                ))
                if title_element.is_displayed():
                    print("Step 8 verification successful - Found title using XPath")
                    return True
            except Exception:
                print("Could not verify title with XPath, trying UiAutomator...")
                
                # Second attempt with UiAutomator
                title_element = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("خلاصه مشخصات سند حمل")'
                )
                if title_element.is_displayed():
                    print("Step 8 verification successful - Found title using UiAutomator")
                    return True
            return False
        except Exception as e:
            print(f"Step 8 verification failed: {str(e)}")
            return False

    def get_captcha_text(self):
        """Get the captcha text from the image"""
        try:
            # First try to find parent container using UiAutomator
            try:
                parent_element = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.ViewGroup").instance(26)'
                )
                
                # Find all TextViews within the parent
                text_elements = parent_element.find_elements(
                    AppiumBy.CLASS_NAME,
                    'android.widget.TextView'
                )
                
                # Find the TextView that contains exactly 4 digits
                for element in text_elements:
                    text = element.text
                    if text.isdigit() and len(text) == 4:
                        print(f"Found captcha text using UiAutomator: {text}")
                        return text
                
                raise Exception("No 4-digit text found in TextViews")
                
            except Exception:
                print("Could not find captcha with UiAutomator, trying XPath...")
                
                # Second attempt with full XPath for parent
                parent_element = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup')
                ))
                
                # Find all TextViews within the parent
                text_elements = parent_element.find_elements(
                    AppiumBy.CLASS_NAME,
                    'android.widget.TextView'
                )
                
                # Find the TextView that contains exactly 4 digits
                for element in text_elements:
                    text = element.text
                    if text.isdigit() and len(text) == 4:
                        print(f"Found captcha text using XPath: {text}")
                        return text
                
                raise Exception("No 4-digit text found in TextViews")
                
        except Exception as e:
            print(f"Failed to get captcha text: {str(e)}")
            return None

    def fill_captcha(self, captcha_text):
        """Fill the captcha text into the input field"""
        try:
            # First attempt with resource-id
            try:
                input_field = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("RNE__Input__text-input")'
                )
                input_field.click()
                input_field.send_keys(captcha_text)
                print("Filled captcha using resource-id")
                return True
            except Exception:
                print("Could not find input field with resource-id, trying UiAutomator instance...")
                
                # Second attempt with UiAutomator
                try:
                    input_field = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.ViewGroup").instance(30)'
                    )
                    input_field.click()
                    input_field.send_keys(captcha_text)
                    print("Filled captcha using UiAutomator instance")
                    return True
                except Exception:
                    print("Could not find input field with UiAutomator instance, trying XPath...")
                    
                    # Third attempt with XPath
                    input_field = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="RNE__Input__text-input"]')
                    ))
                    input_field.click()
                    input_field.send_keys(captcha_text)
                    print("Filled captcha using XPath")
                    return True
        except Exception as e:
            print(f"Failed to fill captcha: {str(e)}")
            return False

    def click_submit(self):
        """Click on the submit button"""
        try:
            # First attempt with content-desc
            try:
                submit_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="صدور سند"]')
                ))
                submit_button.click()
                print("Clicked submit button using content-desc")
                return True
            except Exception:
                print("Could not find submit button by content-desc, trying UiAutomator...")
                
                # Second attempt with UiAutomator
                try:
                    submit_button = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("صدور سند")'
                    )
                    submit_button.click()
                    print("Clicked submit button using UiAutomator")
                    return True
                except Exception:
                    print("Could not find submit button by UiAutomator, trying text...")
                    
                    # Third attempt with text
                    submit_button = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.TextView[@text="صدور سند"]')
                    ))
                    submit_button.click()
                    print("Clicked submit button using text")
                    return True
        except Exception as e:
            print(f"Failed to click submit button: {str(e)}")
            return False

    def confirm_popup(self):
        """Handle the confirmation popup after submit"""
        try:
            # First verify if popup is visible
            try:
                popup_text = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text=" آیا از صدور باربرگ حقیقی اطمینان دارید؟ "]')
                ))
                print("Found confirmation popup using XPath")
            except Exception:
                print("Could not find popup with XPath, trying UiAutomator...")
                popup_text = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text(" آیا از صدور باربرگ حقیقی اطمینان دارید؟ ")'
                )
                print("Found confirmation popup using UiAutomator")

            # Click on confirm button
            try:
                confirm_button = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("بله")'
                )
                confirm_button.click()
                print("Clicked confirm button using UiAutomator")
                return True
            except Exception:
                print("Could not click confirm with UiAutomator, trying XPath...")
                confirm_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="بله"]')
                ))
                confirm_button.click()
                print("Clicked confirm button using XPath")
                return True

        except Exception as e:
            print(f"Failed to handle confirmation popup: {str(e)}")
            return False

    def verify_and_submit(self):
        """Complete summary verification and submission process"""
        try:
            if self.verify_step_title():
                time.sleep(1)  # Wait for animations
                captcha_text = self.get_captcha_text()
                if not captcha_text:
                    return False
                time.sleep(0.5)  # Wait before filling
                if not self.fill_captcha(captcha_text):
                    return False
                time.sleep(0.5)  # Wait before submitting
                if not self.click_submit():
                    return False
                time.sleep(1)  # Wait for popup
                if not self.confirm_popup():
                    return False
                return True
            return False
        except Exception as e:
            print(f"Step 8 summary verification and submission failed: {str(e)}")
            return False 