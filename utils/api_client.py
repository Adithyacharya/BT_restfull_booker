import configparser
import os
import requests
import random
from datetime import datetime, timedelta

class APIClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }

    def modify_booking(self, endpoint, booking_id, data):
        # Use the booking_id dynamically
        url = f"{self.BASE_URL}/{endpoint}/{booking_id}"
        # Send data directly as a dictionary using the `json` parameter
        response = requests.patch(url, headers=self.headers, json=data)
        return response


    def generate_booking(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        print(url)
        response = requests.post(url, headers=self.headers,json=data)
        return response

    @staticmethod
    def generate_dates():
        """
        Generate random check-in and check-out dates.

        Check-in is randomly chosen, and check-out is a few days later.

        Returns:
            list: A list containing the check-in and check-out dates as strings in 'YYYY-MM-DD' format.
        """
        # Define the range for the check-in date
        start_date = datetime.strptime("2018-01-01", "%Y-%m-%d")
        end_date = datetime.strptime("2025-01-01", "%Y-%m-%d")

        # Generate a random check-in date
        random_checkin = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

        # Generate a random check-out date (1 to 10 days after check-in)
        random_checkout = random_checkin + timedelta(days=random.randint(1, 10))

        # Convert dates to 'YYYY-MM-DD' format and return as a list
        return [random_checkin.strftime("%Y-%m-%d"), random_checkout.strftime("%Y-%m-%d")]

    def update_test_data_ini(self,user_data, booking_response, filename='data/test_data.ini'):
        """Update the test_data.ini file with user data, booking information, and total price."""
        # Extract the booking details from the response
        booking_id = booking_response['bookingid']
        booking_details = booking_response['booking']
        total_price = booking_details.get('totalprice', 'N/A')  # Extract total price, default to 'N/A' if not present
        # firstname = booking_details.get('firstname', 'N/A')
        # lastname = booking_details.get('lastname', 'N/A')
        # Initialize the configparser
        config = configparser.ConfigParser()
        # Check if the ini file exists, if not, create it
        if not os.path.exists(filename):
            config['DEFAULT'] = {'test': 'value'}  # Define a default section if needed
            with open(filename, 'w') as configfile:
                config.write(configfile)
        # Read the current ini file
        config.read(filename)
        # If the user section doesn't exist, create it
        if not config.has_section(user_data['username']):
            config.add_section(user_data['username'])

        # Add user data and booking info to the section
        # config.set(user_data['username'], 'firstname', firstname)
        # config.set(user_data['username'], 'lastname', lastname)
        config.set(user_data['username'], 'bookingid', str(booking_id))  # Store the booking ID
        config.set(user_data['username'], 'current_totalprice', str(total_price))  # Store the total price

        # Write the changes back to the ini file
        with open(filename, 'w') as configfile:
            config.write(configfile)

        print(f"Updated {filename} with user {user_data['username']} booking information, total price: {total_price}")

    def delete_booking(self, endpoint,booking_id):
        url = f"{self.BASE_URL}/{endpoint}/{booking_id}"
        response = requests.delete(url, headers=self.headers)
        return response



