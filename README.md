# TMSQAP05-Diploma
Diploma project for AQA python course

###Checklist for

---------------------

### **Login**
- Login page fields
- Login
- Checking the login on ready-made
- Login verification for new random data

### **Registration**
- Registration new user
- Checking checkboxes
- Checking the name field
- Checking the last name field
- Checking the email field
- Checking the password field
- Checking confirm password field
- Checking the register button

### **Changing the password on the user's page**
- Checking fields change password
- Change password

### **Main page**
- Checking main page links

### **Product page**
- Checking the correct link to all products
- Checking the correct link to the health book
- Checking the button to add a product
- Adding a product from the product details page
- Adding a product from the Product list page
- Checking the order and login on new data

Install all requirements:

    pip install -r requirements
    
Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

Launching with Allure
    
    pytest --headless=True --alluredir= 'path to allure result folder'

Browser Selection:
--browser_name=Chrome
or
--browser_name=Firefox

Mode selection:
--headless=True
or
--headless=False

Partial verification is possible:
-m smoke
or
-m fields

----------------------------------------
###Stack
Python,Selenium,Pytest,Allure