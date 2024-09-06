# Python Automation Framework

# Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, PyTest HTML
- Test Data Management - CSV, Excel, JSON,Faker
- for adv API Testcase- jsonschema
- Parallel Execution - x distribute (xdist)


#How to install packages
pip install requests pytest pytest-html faker allure-pytest jsonschema

#How to run parallel execution TC
pip install pytest-xdist
-xdist used for python
-testNG  used for Java Projects

#How to add .gitignore file?
.gitignore> .env related or unnecessary files no need to upload to git, to avaoid that we add this
copy the content from below link:https://www.toptal.com/developers/gitignore/api/pycharm


#how to run the basic Test case 
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s

#To generate report
allure serve allure_result
http://192.168.50.20:60918/index.html

![image](https://github.com/user-attachments/assets/31b498b1-979b-4f95-891f-cf26b6061f8f)

