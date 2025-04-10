from modules.api import drivers_log_api

def test_create_driver_log():
    driver_name = "DRV00001"  # your test driver name
    status = "Wrong Password"  # your test status

    result = drivers_log_api.create_driver_log(driver_name, status)

    if result:
        print("✅ Test Passed: Log created successfully.")
        print(result)
    else:
        print("❌ Test Failed: Could not create log.")

if __name__ == "__main__":
    test_create_driver_log()
