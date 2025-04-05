from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Step0VerificationModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self):
        """Verify if we're on step 0 by checking for the specific text"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="باربرگ حقیقی"]')
            ))
            if title_element.is_displayed():
                print("ما در مرحله 0 هستیم - باربرگ حقیقی مشاهده شد")
                return True
            return False
        except Exception as e:
            print(f"خطا در بررسی عنوان مرحله 0: {str(e)}")
            return False

    def click_continue_button(self):
        """Click on the continue button using different strategies"""
        try:
            # First attempt: Using xpath with content-desc
            continue_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
            ))
            continue_button.click()
            print("دکمه ادامه با استفاده از content-desc کلیک شد")
            return True
        except Exception as e:
            print("جستجوی دکمه ادامه با content-desc ناموفق بود، تلاش با روش دوم...")
            try:
                # Second attempt: Using xpath with text
                continue_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="ادامه"]')
                ))
                continue_button.click()
                print("دکمه ادامه با استفاده از text کلیک شد")
                return True
            except Exception as e:
                print(f"خطا در کلیک دکمه ادامه: {str(e)}")
                return False

    def verify_and_continue(self):
        """Verify the current step and continue if correct"""
        try:
            if self.verify_step_title():
                time.sleep(1)  # کمی صبر برای اطمینان از تکمیل انیمیشن‌ها
                return self.click_continue_button()
            return False
        except Exception as e:
            print(f"خطا در تایید و ادامه مرحله 0: {str(e)}")
            return False 