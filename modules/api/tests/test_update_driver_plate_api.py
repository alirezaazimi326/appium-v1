from modules.api import update_driver_plate_api

def test_update_or_add_plate():
    driver_id = "DRV00002"
    left_number = "22"
    center_number = "333"
    plate_letter = "u"
    ir_number = "44"

    result = update_driver_plate_api.update_or_add_plate(
        driver_id,
        left_number,
        center_number,
        plate_letter,
        ir_number
    )

    if result:
        print("✅ Test Passed: Plate table updated successfully.")
        print(result)
    else:
        print("❌ Test Failed: Could not update plate table.")

if __name__ == "__main__":
    test_update_or_add_plate()
