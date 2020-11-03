from selenium.webdriver import Chrome


def before_all(context):
    path = "C:\\Users\\GOURAV\\Downloads\\chromedriver_win32\\chromedriver.exe"
    context.driver = Chrome(executable_path=path)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


def after_all(context):
    context.driver.close()
