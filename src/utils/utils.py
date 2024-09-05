#contains common utilities
#read data from csv file
#read data from excel file
#set the headers- application/json, application/xml

class Utils(object):

    def common_headers_json(self):
        headers = {
        "Content-Type": "application/json"
    }
        return headers

# in future we will use below functions

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database_file(self):
        pass
