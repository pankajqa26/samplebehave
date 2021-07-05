from behave import *
from selenium import webdriver
import os

@given('I am now new Launch Chrome browser')
def launchnews(context):
    path = str(os.getcwd())
    context.driver = webdriver.Chrome(executable_path= path +"\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://www.data-axle.com/")
    context.driver.get("https://auth.data-axle.com/oauth/authorize?client_id=aa896f8ee71ef28c99a9b997&redirect_uri=https%3A%2F%2Fplatform.data-axle.com%2Fauth_time%2Fcallback")


@then('User must successfully Login to the Home screen')
def step_implogin(context):
    raise NotImplementedError('STEP: Then User must successfully Login to the Home screen')


@then('verify that the user Forget successfully')
def step_impl(context):
    raise NotImplementedError('STEP: Then verify that the user Forget successfully')

