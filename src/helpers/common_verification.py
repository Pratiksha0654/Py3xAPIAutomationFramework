# used to check the response verification like status code, expected vs actual results/expected data
#HTTP Status code
#Data verification
#Headers
#Json Schema


def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed ER!=AR"


def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key !=0, "failed- key is not empty"+key
    assert key >0, "failed- key is greater than zero"
def verify_json_key_for_not_null_token(key):
    assert key !=0, "Failed- key is non empty" +key

def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_response_delete(response):
    assert "created" in response