from modules.api import update_driver_capacity_api

def test_update_driver_capacity():
    driver_id = "DRV00002"
    truck_capacity = 19  # Example value (will come from app in future)

    result = update_driver_capacity_api.update_driver_capacity(driver_id, truck_capacity)

    if result:
        print("✅ Test Passed: Driver capacity updated successfully.")
        print(result)
    else:
        print("❌ Test Failed: Could not update driver capacity.")

if __name__ == "__main__":
    test_update_driver_capacity()
