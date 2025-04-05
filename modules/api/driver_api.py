import requests
from typing import Dict, List, Optional
from config.api_config import (
    DRIVERS_LIST_URL, 
    get_driver_detail_url,
    FRAPPE_API_KEY,
    FRAPPE_API_SECRET
)

class DriverAPI:
    def __init__(self):
        """Initialize the Driver API handler"""
        self.session = requests.Session()
        # Set up authentication
        self.session.auth = (FRAPPE_API_KEY, FRAPPE_API_SECRET)
        # Set common headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def get_drivers_list(self) -> List[str]:
        """Get list of all driver IDs"""
        try:
            response = self.session.get(DRIVERS_LIST_URL)
            response.raise_for_status()
            data = response.json()
            return [driver["name"] for driver in data.get("data", [])]
        except requests.RequestException as e:
            print(f"Error fetching drivers list: {str(e)}")
            return []

    def get_driver_details(self, driver_id: str) -> Optional[Dict]:
        """Get detailed information for a specific driver"""
        try:
            url = get_driver_detail_url(driver_id)
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json().get("data")
            
            if data:
                return {
                    "user_name": data.get("user_name"),
                    "password": data.get("password"),
                    "receiver_full_name": data.get("receiver_full_name"),
                    "receiver_phone_number": data.get("receiver_phone_number"),
                    "sender_full_name": data.get("sender_full_name"),
                    "sender_phone_number": data.get("sender_phone_number"),
                    "product_name": data.get("product_name"),
                    "weight": data.get("weight"),
                    "packaging_type": data.get("packaging_type"),
                    "cargo_value": data.get("cargo_value")
                }
            return None
        except requests.RequestException as e:
            print(f"Error fetching driver details for {driver_id}: {str(e)}")
            return None

    def get_driver_by_phone(self, phone_number: str) -> Optional[Dict]:
        """Find driver details by phone number"""
        try:
            # First get all drivers
            drivers = self.get_drivers_list()
            
            # Then check each driver's details
            for driver_id in drivers:
                driver_details = self.get_driver_details(driver_id)
                if driver_details and driver_details.get("user_name") == phone_number:
                    return driver_details
            
            print(f"No driver found with phone number: {phone_number}")
            return None
        except Exception as e:
            print(f"Error searching for driver by phone: {str(e)}")
            return None 