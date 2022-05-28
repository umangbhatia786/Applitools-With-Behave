from selenium.webdriver.common.by import By
from features.pages.page_base import PageBase
from time import sleep


class SearchPageLocator(object):
    SEARCH_BAR = (By.ID, 'searchBar')
    BOOK_TITLES = (By.CSS_SELECTOR, '#productList li a h2')
    AGILE_TESTING_BOOK_REGION = (By.ID, 'pid3')
    GOOGLE_BOOK_REGION = (By.ID, 'pid4')


class SearchPage(PageBase):

    def filter_books(self, book_name):
        self.enter_text(book_name, SearchPageLocator.SEARCH_BAR)
        sleep(5)

    def verify_visible_books_by_title(self, expected_title):
        elements = self.return_element_list(SearchPageLocator.BOOK_TITLES)

        for element in elements:
            if expected_title in element.text:
                return True
        return False

    def return_web_element_book(self, search_text):
        if search_text == 'Google':
            element = self.return_element(SearchPageLocator.GOOGLE_BOOK_REGION)
        elif search_text == 'Agile':
            element = self.return_element(SearchPageLocator.AGILE_TESTING_BOOK_REGION)
        return element
