from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@given(u'User move cursor to the Job Menu Text')
def step_impl(context):
    admin_text = (By.XPATH, "//a[@id='menu_admin_Job']")
    element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(admin_text))
    ActionChains(context.driver).move_to_element(element).perform()


@when(u'User move cursor to the Job Menu Text')
def step_impl(context):
    admin_text = (By.XPATH, "//a[@id='menu_admin_Job']")
    element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(admin_text))
    ActionChains(context.driver).move_to_element(element).perform()


@when(u'Click on the Job Title Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='menu_admin_viewJobTitleList']").click()


@when(u'Click Add Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='btnAdd']").click()


@when(u'Enter Job Title "Software Engineers"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='jobTitle_jobTitle']").send_keys("Software Engineers")


@when(u'Enter Job Description "Testing Engineer"')
def step_impl(context):
    context.driver.find_element_by_xpath("//textarea[@id='jobTitle_jobDescription']").send_keys(
        "Software Engineers")


@when(u'Select Job File')
def step_impl(context):
    filename = "E:/py.txt"
    context.driver.find_element_by_xpath("//input[@id='jobTitle_jobSpec']").send_keys(filename)


@then(u'Click Save Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='btnSave']").click()


@when(u'Click on the Pay Grade Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='menu_admin_viewPayGrades']").click()


@then(u'Check Pay Grade Column Presence')
def step_impl(context):
    table_id = (By.XPATH, "//table[@id='resultTable']")
    column_status = (By.XPATH, "//table[@id='resultTable']//a[contains(text(),'Pay Grade')]")
    for col in table_id:
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(column_status))
        assert element.text == "Pay Grade"


@then(u'Click Add Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='btnAdd']").click()


@then(u'Enter Pay Grade Name "Engineers"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='payGrade_name']").send_keys("Engineers")


@when(u'Click on the Employment Status Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='menu_admin_employmentStatus']").click()


@then(u'Check Employment Status Column Presence')
def step_impl(context):
    table_id = (By.XPATH, "//table[@id='resultTable']")
    column_status = (By.XPATH, "//table[@id='resultTable']//span[contains(text(),'Employment Status')]")
    for col in table_id:
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(column_status))
        assert element.text == "Employment Status"


@then(u'Enter Employment Name "Engineers"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='empStatus_name']").send_keys("Engineers")


@when(u'Click on the Job Category Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='menu_admin_jobCategory']").click()


@then(u'Check Job Category Column Presence')
def step_impl(context):
    table_id = (By.XPATH, "//table[@id='resultTable']")
    column_status = (By.XPATH, "//table[@id='resultTable']//span[contains(text(),'Job Category')]")
    for col in table_id:
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(column_status))
        assert element.text == "Job Category"


@then(u'Enter Job Category Name "Engineers"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='jobCategory_name']").send_keys("Engineers")


@when(u'Click on the Work Shift Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='menu_admin_workShift']").click()


@then(u'Check Shift Name Column Presence')
def step_impl(context):
    table_id = (By.XPATH, "//table[@id='resultTable']")
    column_status = (By.XPATH, "//table[@id='resultTable']//span[contains(text(),'Shift Name')]")
    for col in table_id:
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(column_status))
        assert element.text == "Shift Name"


@then(u'Enter Work Shift Name "Engineers"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='workShift_name']").send_keys("Engineers")


@then(u'Select Work Shift Timings From')
def step_impl(context):
    emp_status = "//select[@id='workShift_workHours_from']"
    ele = context.driver.find_element_by_xpath(emp_status)
    sel = Select(ele)
    sel.select_by_value("08:00")


@then(u'Select Work Shift Timings To')
def step_impl(context):
    emp_status = "//select[@id='workShift_workHours_to']"
    ele = context.driver.find_element_by_xpath(emp_status)
    sel = Select(ele)
    sel.select_by_value("18:00")


@then(u'Check Presence Of Duration')
def step_impl(context):
    # duration = (By.XPATH, "//input[@class='time_range_duration']")
    element = context.driver.find_element_by_xpath("//input[@class='time_range_duration']").get_attribute("value")
    print(element)
    # element = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located(duration))
    assert element == "10"


@then(u'Select Available Employee')
def step_impl(context):
    emp_status = "//select[@id='workShift_availableEmp']"
    ele = context.driver.find_element_by_xpath(emp_status)
    sel = Select(ele)
    sel.select_by_visible_text("Robert Craig")


@then(u'Click AddEmployee Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@id='btnAssignEmployee']").click()


@then(u'Select Assigned Employee')
def step_impl(context):
    emp_status = "//select[@id='workShift_assignedEmp']"
    ele = context.driver.find_element_by_xpath(emp_status)
    sel = Select(ele)
    sel.select_by_visible_text("Robert Craig")
