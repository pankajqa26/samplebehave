from behave import *
from selenium import webdriver


@given('i launch chrome browser')
def launch(context):
    context.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://www.data-axle.com/")
    context.driver.get("https://auth.data-axle.com/oauth/authorize?client_id=aa896f8ee71ef28c99a9b997&redirect_uri=https%3A%2F%2Fplatform.data-axle.com%2Fauth_time%2Fcallback")
    context.driver.get("https://auth.data-axle.com/password_resets/new")

@when('open DataAxel Forget {email}')
def openForget(context, email):

    context.driver.find_element_by_id("email").send_keys(email)



@when('click on Next Button')
def step_impl(context):
    context.driver.find_element_by_name("commit").click()


@then('close browsers')
def closeBrowsers(context):
    context.driver.close()