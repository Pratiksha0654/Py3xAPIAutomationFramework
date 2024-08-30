import allure
import pytest


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("verify that create booking Status and BookingId should not be null")
    @allure.description(
        "Creating a booking from payload and verify that booking id should not be null and status is 200")
    def test_create_booking_positive(self):
        pass
