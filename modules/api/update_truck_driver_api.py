import requests
from config import api_config

session = requests.Session()
session.headers.update({
    "Authorization": f"token {api_config.FRAPPE_API_KEY}:{api_config.FRAPPE_API_SECRET}"
})

def update_or_add_truck_driver(driver_id: str, name1: str, national_id: str):
    """
    Update existing truck driver if exists, otherwise add a new driver to the drivers_table.

    Args:
        driver_id (str): Driver ID, e.g., 'DRV00002'
        name1 (str): Name of the truck driver
        national_id (str): National ID of the truck driver
    """
    driver_url = api_config.get_driver_detail_url(driver_id)

    try:
        # Step 1: Fetch current driver data
        response = session.get(driver_url)
        response.raise_for_status()
        driver_data = response.json().get("data", {})

        drivers_table = driver_data.get("drivers_table", [])

        # Step 2: Check if driver exists in table
        existing_driver = None
        for driver in drivers_table:
            if (driver.get("name1") == name1 and
                driver.get("national_id") == national_id):
                existing_driver = driver
                break

        # Step 3: Prepare updated drivers_table
        if existing_driver:
            print(f"[Truck Driver] Existing truck driver found, updating it (idx: {existing_driver.get('idx')}).")
            for driver in drivers_table:
                if driver["name"] == existing_driver["name"]:
                    driver.update({
                        "name1": name1,
                        "national_id": national_id,
                        "idx": driver.get("idx", 1)  # Ensure idx stays
                    })
        else:
            new_idx = len(drivers_table) + 1
            print(f"[Truck Driver] No existing driver found, adding new driver at idx {new_idx}.")
            drivers_table.append({
                "doctype": "Truck Drivers",
                "name1": name1,
                "national_id": national_id,
                "idx": new_idx
            })

        # Step 4: Send update to Frappe
        payload = {
            "drivers_table": drivers_table
        }

        update_response = session.put(driver_url, json=payload)
        update_response.raise_for_status()

        print(f"[Truck Driver] Driver '{driver_id}' drivers_table updated successfully.")
        return update_response.json()

    except requests.RequestException as e:
        print(f"[Truck Driver] Failed to update drivers_table for driver '{driver_id}'. Error: {e}")
        return None
