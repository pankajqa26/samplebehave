from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    context.driver.maximize_window()


@when('open DataAxel Login')
def openLogin(context):
    context.driver.get("https://www.data-axle.com/")

    #print(driver.title)
    #print(driver.current_url)
    context.driver.get("https://www.data-axle.com/what-we-do/")

@then('verify that the user login on page')
def verifyLogin(context):
    context.driver.get("https://auth.data-axle.com/oauth/authorize?client_id=aa896f8ee71ef28c99a9b997&redirect_uri=https%3A%2F%2Fplatform.data-axle.com%2Fauth_time%2Fcallback")
    context.driver.find_element_by_name("commit").click()
    context.driver.get("https://auth.data-axle.com/oauth/authorize?client_id=aa896f8ee71ef28c99a9b997&redirect_uri=https%3A%2F%2Fplatform.data-axle.com%2Fauth_time%2Fcallback")
    context.driver.find_element_by_id("email").send_keys("hhh")
    context.driver.get("https://auth.data-axle.com/oauth/authorize?client_id=aa896f8ee71ef28c99a9b997&redirect_uri=https%3A%2F%2Fplatform.data-axle.com%2Fauth_time%2Fcallback")
    context.driver.find_element_by_id("email").send_keys("pankajrajwaniya@gmail.com")
    context.driver.find_element_by_id("password").send_keys("Kipl@123")
    context.driver.find_element_by_name("commit").click()
   # assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()
