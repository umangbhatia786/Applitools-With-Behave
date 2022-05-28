from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from features.pages.test_base import TestBase
from assertpy import assert_that

test_base = TestBase()


@given(u'We enter the search text as {text}')
def step_impl(context, text):
    context.search_text = text
    context.search_page.filter_books(text)


@then(u'We verify the books by title as {title}')
def step_impl(context, title):
    context.eyes.validate_window(context.scenario.name, 'filter-text')
    result = context.search_page.verify_visible_books_by_title(title)
    assert_that(result).is_equal_to(True)


@then(u'Verify the book result region using applitools eyes')
def step_impl(context):
    book_el = context.search_page.return_web_element_book(context.search_text)
    context.eyes.validate_region(context.scenario.name, book_el, 'filter-region')