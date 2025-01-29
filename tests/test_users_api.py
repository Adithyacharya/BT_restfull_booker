import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()


@pytest.mark.parametrize("user", ["user1", "user2", "user3"])
def test_generate_booking(api_client, load_user_data, user):
    try:
        # Load user data for the current test
        user_data = load_user_data[user]
        response = api_client.generate_booking("booking", user_data)
        print(f"API response for {user}: {response.json()}")
        # Assert that the API call was successful
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert True, f"Booking generated successfully for user '{user}'"
        # Update the test_data.ini file with the user and booking data
        user_data['username'] = user  # Set the username based on the parameterized input
        api_client.update_test_data_ini(user_data, response.json())


    except KeyError as e:
        pytest.fail(f"User '{user}' data not found: {str(e)}", pytrace=True)
    except Exception as e:
        pytest.fail(f"An error occurred during the test for user '{user}': {str(e)}", pytrace=True)


def test_modify_test1(api_client, read_from_ini):

    bookingid = read_from_ini("user1", "bookingid")
    totalprice = int(read_from_ini("user1", "modify_totalprice"))
    depositpaid= read_from_ini("user1","depositpaid")
    check_in_date=api_client.generate_dates()[0]
    check_out_date=api_client.generate_dates()[1]
    additionalneeds= read_from_ini("user1", "additionalneeds")
    print(check_in_date, check_out_date)

    userdata = {
        "totalprice": totalprice,  # Pass as integer
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": check_in_date,
            "checkout": check_out_date,
        },
        "additionalneeds": additionalneeds

    }

    # Make the API call to modify the booking
    response = api_client.modify_booking("booking", bookingid, userdata)

    # Validate response
    assert response.status_code == 200, f"Failed to modify booking {bookingid}"
    print(f"Booking {bookingid} modified successfully. Response: {response.json()}")

def test_modify_test2(api_client, read_from_ini):

    bookingid = read_from_ini("user2", "bookingid")
    totalprice = int(read_from_ini("user2", "modify_totalprice"))
    depositpaid= read_from_ini("user2","depositpaid")
    check_in_date=api_client.generate_dates()[0]
    check_out_date=api_client.generate_dates()[1]
    additionalneeds= read_from_ini("user2", "additionalneeds")
    print(check_in_date, check_out_date)

    userdata = {
        "totalprice": totalprice,  # Pass as integer
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": check_in_date,
            "checkout": check_out_date,
        },
        "additionalneeds": additionalneeds

    }

    # Make the API call to modify the booking
    response = api_client.modify_booking("booking", bookingid, userdata)

    # Validate response
    assert response.status_code == 200, f"Failed to modify booking {bookingid}"
    print(f"Booking {bookingid} modified successfully. Response: {response.json()}")


def test_delete_booking(api_client, read_from_ini):
    booking_id = read_from_ini("user3", "bookingid")  # Read booking ID from INI file
    response = api_client.delete_booking("booking",booking_id)

    assert response.status_code == 201, f"Failed to delete booking {booking_id}, got {response.status_code}"
    print(f"Booking {booking_id} deleted successfully.")
