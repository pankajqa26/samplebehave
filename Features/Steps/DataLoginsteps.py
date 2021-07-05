from behave import *
from selenium import webdriver
import os


@given('i am now launch chrome browser')
def launchnew(context):
    path = str(os.getcwd())
    context.driver = webdriver.Chrome(executable_path= path +"\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://www.data-axle.com/")
    context.driver.get("https://auth.data-axle.com/oauth/authorize?client_id=aa896f8ee71ef28c99a9b997&redirect_uri=https%3A%2F%2Fplatform.data-axle.com%2Fauth_time%2Fcallback")


@when('open DataAxle Emails {email} passw {password}')
def openLoginm(context, email, password):
    context.driver.find_element_by_id("email").send_keys(email)
    context.driver.find_element_by_id("password").send_keys(password)


@when('click on Submit Button')
def step_implm(context):
    context.driver.find_element_by_name("commit").click()


@then('close my browsers')
def closeBrowserso(context):
    context.driver.close()
