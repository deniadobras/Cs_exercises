from behave import *

use_step_matcher("re")


@given("I am on google search page")
def step_impl(context):
    print("I am on google search page")

@when("I type in text to search")
def step_impl(context):
    print("I type in text to search")


@step("I hit search button")
def step_impl(context):
    print("I hit search button")


@then("I should be on the search results page")
def step_impl(context):
    print("I should be on the search results page")