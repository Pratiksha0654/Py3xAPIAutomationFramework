import allure
import pytest
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("verify that create booking Status and BookingId should not be null")
    @allure.description(
        "Creating a booking from payload and verify that booking id should not be null and status is 200")
    def test_create_booking_positive(self):
        response = post_request(
            url=APIConstants().create_booking_url(),
            auth= None,
            headers= Utils().common_headers_json(),

            payload= payload_create_booking(),
            in_json=False
        )
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(booking_id)
