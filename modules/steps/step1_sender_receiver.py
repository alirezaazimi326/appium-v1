from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

# Add the parent directory to the Python path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class Step1SenderReceiverModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.driver_details = None

    def set_driver_details(self, driver_details):
        """Set driver details received from login module"""
        self.driver_details = {
            'sender': {
                'full_name': driver_details['sender_full_name'],
                'phone_number': driver_details['sender_phone_number']
            },
            'receiver': {
                'full_name': driver_details['receiver_full_name'],
                'phone_number': driver_details['receiver_phone_number']
            }
        }

    def verify_step_title(self, expected_title="مشخصات فرستنده و گیرنده"):
        """Verify if we're on the sender/receiver step"""
        try:
        # Try with UiSelector first
            try:
                title_element = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{expected_title}")'
                )))
                if title_element.is_displayed():
                    print(f"Verified step 1 using UiSelector: {expected_title}")
                    return True
            except Exception:
                print("UiSelector check failed, trying XPath...")

        # Fallback to XPath
            try:
                title_element = self.wait.until(EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    f'//android.widget.TextView[@text="{expected_title}"]'
                )))
                if title_element.is_displayed():
                    print(f"Verified step 1 using XPath: {expected_title}")
                    return True
            except Exception:
                pass

            print(f"Step 1 title not found: {expected_title}")
            return False

        except Exception as e:
            print(f"Error verifying step 1 title: {str(e)}")
            return False


    def fill_sender_details(self, sender_info):
        """Fill in the sender details"""
        try:
            # Fill sender full name - using index since it's the first input field
            name_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @index="0"]')
            ))
            name_field.clear()
            name_field.send_keys(sender_info['full_name'])
            print(f"Entered sender name: {sender_info['full_name']}")

            time.sleep(0.5)  # Add a small delay before interacting with the phone field

            # Find all input fields and get the second one for phone
            input_fields = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            if len(input_fields) >= 2:
                phone_field = input_fields[1]  # Get the second input field
                phone_field.clear()
                phone_field.send_keys(sender_info['phone_number'])
                print(f"Entered sender phone: {sender_info['phone_number']}")
            else:
                print("Could not find phone number field")
                return False
            
            return True
        except Exception as e:
            print(f"Error filling sender details: {str(e)}")
            return False

    def fill_receiver_details(self, receiver_info):
        """Fill in the receiver details"""
        try:
            # Fill receiver full name using exact bounds
            name_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="RNE__Input__text-input"])[6]')
            ))
            name_field.clear()
            name_field.send_keys(receiver_info['full_name'])
            print(f"Entered receiver name: {receiver_info['full_name']}")

            time.sleep(0.5)  # Add a small delay before interacting with the phone field

            # Fill receiver phone number using exact bounds
            phone_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="RNE__Input__text-input"])[7]')
            ))
            phone_field.clear()
            phone_field.send_keys(receiver_info['phone_number'])
            print(f"Entered receiver phone: {receiver_info['phone_number']}")
            
            return True
        except Exception as e:
            print(f"Error filling receiver details: {str(e)}")
            return False

    def click_continue_button(self):
        """Click on the continue button"""
        try:
            # Try first with content-desc and bounds
            continue_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
            ))
            continue_button.click()
            print("Clicked continue button using content-desc and bounds")
        except Exception as e:
            print("Could not find continue button by content-desc and bounds, trying alternative method...")
            try:
                # Fallback to just content-desc
                continue_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="ادامه"]')
                ))
                continue_button.click()
                print("Clicked continue button using accessibility ID")
            except Exception as e:
                print(f"Error clicking continue button: {str(e)}")
                raise

    def fill_and_continue(self):
        """Fill all details and continue to next step"""
        try:
            if not self.verify_step_title():
                return False

            if not self.driver_details:
                print("No driver details available. Please set driver details first.")
                return False

            if not self.fill_sender_details(self.driver_details['sender']):
                return False
            if not self.fill_receiver_details(self.driver_details['receiver']):
                return False
                
            time.sleep(1)  # Wait for any animations
            self.click_continue_button()
            return True
        except Exception as e:
            print(f"Step 1 fill and continue failed with error: {str(e)}")
            return False 