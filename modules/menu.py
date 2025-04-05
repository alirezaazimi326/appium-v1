from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MenuModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_menu_icon(self):
        """Click on the menu icon"""
        try:
            # Try first with class and bounds
            menu_icon = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="باربرگ حقیقی"]/android.widget.ImageView')
            ))
            menu_icon.click()
            print("Clicked menu icon using bounds")
        except Exception as e:
            # Try alternative method with just the class and index
            try:
                menu_icon = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="باربرگ حقیقی"]')
                ))
                menu_icon.click()
                print("Clicked menu icon using class and index")
            except Exception as e:
                print(f"Error clicking menu icon: {str(e)}")
                raise

    def wait_for_menu_to_open(self, timeout=5):
        """Wait for menu animation to complete"""
        time.sleep(1)  # Short wait for animation

    def click_and_wait(self):
        """Click on menu icon and wait for it to open"""
        try:
            self.click_menu_icon()
            self.wait_for_menu_to_open()
            print("منو باز شد و منتظر ماندیم")
            return True
        except Exception as e:
            print(f"خطا در باز کردن منو: {str(e)}")
            return False
