from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@when(u'User navigated to the Login Page')
def step_impl(context):
    forgot_password_text = (By.XPATH, "//a[contains(text(),'Forgot your password?')]")
    element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(forgot_password_text))
    assert element.text == "Forgot your password?"


@when(u'User enters username "Admin"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")


@when(u'User enters password "admin123"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")


@when(u'User click on the Login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='btnLogin']").click()


@then(u'User should be Logged In Successfully')
def step_impl(context):
    pending_leave_request = (By.XPATH, "//legend[contains(text(),'Pending Leave Requests')]")
    element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(pending_leave_request))
    assert element.text == "Pending Leave Requests"


@given(u'User move cursor to Admin')
def step_impl(context):
    admin_text = (By.XPATH, "//b[contains(text(),'Admin')]")
    element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(admin_text))
    ActionChains(context.driver).move_to_element(element).perform()


@when(u'User move cursor to the User Management Text')
def step_impl(context):
    user_management_text = (By.XPATH, "//a[@id='menu_admin_UserManagement']")
    element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(user_management_text))
    ActionChains(context.driver).move_to_element(element).perform()


@when(u'Click on the Users Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']").click()


@when(u'Enter username "Admin"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='searchSystemUser_userName']").send_keys("Admin")


@when(u'Select user Role from drop down')
def step_impl(context):
    user_role = "//select[@id='searchSystemUser_userType']"
    ele = context.driver.find_element_by_xpath(user_role)
    sel = Select(ele)
    sel.select_by_visible_text("Admin")


@when(u'Enter Employee Name')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='searchSystemUser_employeeName_empName']").send_keys("Admin")


@when(u'Select Status from Drop down')
def step_impl(context):
    emp_status = "//select[@id='searchSystemUser_status']"
    ele = context.driver.find_element_by_xpath(emp_status)
    sel = Select(ele)
    sel.select_by_visible_text("Enabled")


@when(u'Click on the Search Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='searchBtn']").click()


@when(u'Search Result Displayed')
def step_impl(context):
    table_id = (By.XPATH, "//table[@id='resultTable']")
    column_status = (By.XPATH, "//a[@class='null'][contains(text(),'Status')]")
    for col in table_id:
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(column_status))
        assert element.text == "Status"


@then(u'Verify the Values of Status Column')
def step_impl(context):
    table_id = (By.XPATH, "//table[@id='resultTable']")
    column_value = (By.XPATH, "//tr[@class='odd']//td[contains(text(),'Enabled')]")
    for col in table_id:
        web_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(column_value))
        assert web_element.text == "Enabled"
