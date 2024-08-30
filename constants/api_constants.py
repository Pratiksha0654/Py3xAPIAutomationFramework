#APIConstants - class which contain all the endpoints
#Keep all URL
#Base UEL, Baspath

class APIConstants(object):
    def base_url(self):
        return"https://restful-booker.herokuapp.com"

    def create_booking_url(self):
        return"https://restful-booker.herokuapp.com/booking"


    def create_token_url(self):
        return"https://restful-booker.herokuapp.com/auth"

    #update/delete/partial update----booking Id
    def patch_put_delete_url(booking_id):
        return"https://restful-booker.herokuapp.com/booking" + str(booking_id)