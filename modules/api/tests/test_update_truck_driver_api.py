from modules.api import update_truck_driver_api

def test_update_or_add_truck_driver():
    driver_id = "DRV00001"
    name1 = "alireza"
    national_id = "4160701914"

    result = update_truck_driver_api.update_or_add_truck_driver(
        driver_id,
        name1,
        national_id
    )

    if result:
        print("✅ Test Passed: Truck driver table updated successfully.")
        print(result)
    else:
        print("❌ Test Failed: Could not update truck driver table.")

if __name__ == "__main__":
    test_update_or_add_truck_driver()
