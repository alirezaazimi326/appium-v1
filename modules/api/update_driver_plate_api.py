import requests
from config import api_config

session = requests.Session()
session.headers.update({
    "Authorization": f"token {api_config.FRAPPE_API_KEY}:{api_config.FRAPPE_API_SECRET}"
})

def update_or_add_plate(driver_id: str, left_number: str, center_number: str, plate_letter: str, ir_number: str):
    """
    Update existing plate if exists (by matching plate details), otherwise add a new plate row to the plate_table.

    Args:
        driver_id (str): Driver ID, e.g., 'DRV00002'
        left_number (str): 2_left_number
        center_number (str): 3_center_number
        plate_letter (str): plate_letter
        ir_number (str): 2_ir_number
    """
    driver_url = api_config.get_driver_detail_url(driver_id)

    try:
        # Step 1: Fetch current driver data
        response = session.get(driver_url)
        response.raise_for_status()
        driver_data = response.json().get("data", {})

        plate_table = driver_data.get("plate_table", [])

        # Step 2: Check if plate exists
        existing_plate = None
        for plate in plate_table:
            if (plate.get("2_left_number") == left_number and
                plate.get("3_center_number") == center_number and
                plate.get("plate_letter") == plate_letter and
                plate.get("2_ir_number") == ir_number):
                existing_plate = plate
                break

        # Step 3: Prepare updated plate table
        if existing_plate:
            print(f"[Plate] Existing plate found, updating it (idx: {existing_plate.get('idx')}).")
            for plate in plate_table:
                if plate["name"] == existing_plate["name"]:
                    plate.update({
                        "2_left_number": left_number,
                        "3_center_number": center_number,
                        "plate_letter": plate_letter,
                        "2_ir_number": ir_number,
                        "idx": plate.get("idx", 1)  # Ensure idx stays
                    })
        else:
            new_idx = len(plate_table) + 1
            print(f"[Plate] No existing plate found, adding new plate at idx {new_idx}.")
            plate_table.append({
                "doctype": "License plate",
                "2_left_number": left_number,
                "3_center_number": center_number,
                "plate_letter": plate_letter,
                "2_ir_number": ir_number,
                "idx": new_idx
            })

        # Step 4: Send update to Frappe
        payload = {
            "plate_table": plate_table
        }

        update_response = session.put(driver_url, json=payload)
        update_response.raise_for_status()

        print(f"[Plate] Driver '{driver_id}' plate_table updated successfully.")
        return update_response.json()

    except requests.RequestException as e:
        print(f"[Plate] Failed to update plate_table for driver '{driver_id}'. Error: {e}")
        return None
