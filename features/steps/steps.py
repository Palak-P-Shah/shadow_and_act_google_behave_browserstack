import time
from behave import *
from google_search_page import *
from common_pages import *


@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)


@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)


@then('title becomes "{title}"')
def step(context, title):
    assert context.browser.title == title


@then(u'page contains "{body}"')
def step(context, body):
    assert body in context.browser.page_source


@given('the browser is launched and navigating to the Google.com page')
def step_impl(context):
    navigate_to_google_page(context.browser)


@then('navigate to the Google.com page')
def step_impl(context):
    navigate_to_google_page(context.browser)


@then('search for "Shadow & Act" keyword')
def step_impl(context):
    search_keyword(context.browser, "Shadow & Act")


@then('Navigate to the Shadow&Act application page from the Google search results')
def step_impl(context):
    launch_app(context.browser)


@then('verify the application is launched successfully')
def step_impl(context):
    post_page_load_pop_up(context.browser)


@then('navigate to the Film page')
def step_impl(context):
    verify_particular_page(context.browser, "FILM")


@then('verify if all the article links are working as expected on the Film page')
def step_impl(context):
    verify_each_article(context.browser, "FILM", "Film")


@then('verify if the Load More stories button work as expected, also verify the links to the articles works as expected')
def step_impl(context):
    verify_number_of_articles(context.browser, "Film")
    verify_each_article(context.browser, "FILM", "Film")


@then('verify if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected')
def step_impl(context):
    verify_number_of_articles(context.browser, "Film")
    verify_number_of_articles(context.browser, "Film")
    verify_each_article(context.browser, "FILM", "Film")


@then('verify footer section is present and displayed')
def step_impl(context):
    verify_footer_presence(context.browser)


@then('close the browser')
def step_impl(context):
    context.browser.quit()
