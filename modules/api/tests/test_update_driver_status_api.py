from modules.api import update_driver_status_api

def test_update_driver_status():
    driver_id = "DRV00002"
    new_status = "Normal"

    result = update_driver_status_api.update_driver_status(driver_id, new_status)

    if result:
        print("✅ Test Passed: Driver status updated successfully.")
        print(result)
    else:
        print("❌ Test Failed: Could not update driver status.")

if __name__ == "__main__":
    test_update_driver_status()
