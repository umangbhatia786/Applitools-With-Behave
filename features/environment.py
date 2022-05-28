from selenium import webdriver

from features.EyesManager import EyesManager
from features.browser import Browser
from behave import *
from features.pages.search_page import SearchPage


def before_all(context):
    context.search_page = SearchPage()
    context.eyes = EyesManager()

# def after_all(context):
#
#     print('====== Closing Browser Session ======')


def before_scenario(context, scenario):
    print('===Before Scenario===' + str(scenario))
    context.browser = Browser()


def after_scenario(context, scenario):
    print('===After Scenario===' + str(scenario))
    # context.browser = None
    context.browser.closeBrowser()
