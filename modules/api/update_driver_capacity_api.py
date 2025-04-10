import requests
from math import floor
from config import api_config

session = requests.Session()
session.headers.update({
    "Authorization": f"token {api_config.FRAPPE_API_KEY}:{api_config.FRAPPE_API_SECRET}"
})

def update_driver_capacity(driver_id: str, truck_capacity: int):
    """
    Update truck_capacity and cargo_weight in the Drivers Doctype.

    Args:
        driver_id (str): Driver ID, e.g., 'DRV00002'
        truck_capacity (int): Truck capacity value (will be read from app later)
    """
    try:
        # Step 1: Calculate cargo weight
        cargo_weight = floor(truck_capacity * 0.6)

        # Step 2: Prepare payload
        payload = {
            "truck_capacity": truck_capacity,
            "cargo_weight": cargo_weight
        }

        driver_url = api_config.get_driver_detail_url(driver_id)

        # Step 3: Send update to Frappe
        response = session.put(driver_url, json=payload)
        response.raise_for_status()

        print(f"[Driver Capacity] Updated driver '{driver_id}': truck_capacity={truck_capacity}, cargo_weight={cargo_weight}")
        return response.json()

    except requests.RequestException as e:
        print(f"[Driver Capacity] Failed to update driver '{driver_id}'. Error: {e}")
        return None
