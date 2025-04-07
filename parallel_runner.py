from multiprocessing import Process
from appium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from modules.before_login import BeforeLoginModule
from modules.steps_handler import StepsHandler
from modules.api.driver_api import DriverAPI


def run_bot(avd_name, port, drivers):
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'avd': avd_name,
        'app': os.path.join(os.getcwd(), 'com.transport.apk'),
        'noReset': True,
        'newCommandTimeout': 3600,
        'platformVersion': '14.0',
        'autoGrantPermissions': True
    }

    try:
        driver = webdriver.Remote(f'http://127.0.0.1:{port}', desired_caps)
        wait = WebDriverWait(driver, 20)

        def is_app_running():
            return driver.current_package == 'com.transport'

        if not is_app_running():
            print(f"[{avd_name}] Launching app...")
            driver.launch_app()
        else:
            print(f"[{avd_name}] App is already open.")

        before_login = BeforeLoginModule(driver)
        if not before_login.click_continue():
            raise Exception(f"[{avd_name}] Failed to click initial continue button")

        steps_handler = StepsHandler(driver)
        api = DriverAPI()

        for driver_id in drivers:
            print(f"[{avd_name}] Processing driver {driver_id}")
            driver_details = api.get_driver_details(driver_id)
            if driver_details:
                if steps_handler.process_driver(driver_details):
                    print(f"[{avd_name}] Successfully processed driver {driver_id}")
                else:
                    print(f"[{avd_name}] Failed to process driver {driver_id}")
            else:
                print(f"[{avd_name}] Could not get details for driver {driver_id}")

    except Exception as e:
        print(f"[{avd_name}] Error: {str(e)}")

    finally:
        driver.quit()
        print(f"[{avd_name}] Session ended.")


if __name__ == "__main__":
    api = DriverAPI()
    drivers_list = api.get_drivers_list()

    if not drivers_list:
        print("No drivers found.")
        exit()

    # Split the driver list in half
    mid_index = len(drivers_list) // 2
    drivers1 = drivers_list[:mid_index]
    drivers2 = drivers_list[mid_index:]

    # Start two processes for two emulators
    p1 = Process(target=run_bot, args=("Pixel_7_Edited_API_34_Num_1", 4723, drivers1))
    p2 = Process(target=run_bot, args=("Pixel_7_Edited_API_34_Num_2", 4725, drivers2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("✅ Both emulators finished processing.")
