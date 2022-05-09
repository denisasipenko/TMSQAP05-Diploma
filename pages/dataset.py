import time


def register_dataset():
    first_name = str(time.time())
    last_name = str(time.time())
    email = str(time.time()) + "@mail.com"
    password = "testtest"
    return first_name, last_name, email, password


class TestDatasets:
    email = "testdemowebshop@mail.com"
    password = "testshop1122"
    new_password = "testWebshop1122"
    city = "Tula"
    address1 = "street1"
    zip_code = "200100"
    phone = "9379992"