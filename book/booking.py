import os

from book.config import URL
from selenium import webdriver
from book.booking_filterations import BookingFilterations
from book.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Seleniumdrivers\chromedriver.exe", teardown=False):
        super(Booking, self).__init__()
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += os.pathsep + self.driver_path
        self.implicitly_wait(15)
        self.maximize_window()

    def get_land_page(self):
        self.get(URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def change_currency(self, currency='USD'):
        self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        ).click()
        self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        ).click()

    def enter_location(self, location):
        search_field = self.find_element_by_id("ss")
        search_field.clear()
        search_field.send_keys(location)

        self.find_element_by_css_selector(
            'li[data-i="0"]'
        ).click()

    def select_dates(self, check_in_dates, check_out_dates):
        self.find_element_by_css_selector(
            f'td[data-date="{check_in_dates}"]'
        ).click()

        self.find_element_by_css_selector(
            f'td[data-date="{check_out_dates}"]'
        ).click()

    def number_of_adults(self, count=1):
        self.find_element_by_id("xp__guests__toggle").click()
        decrease = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        while True:
            decrease.click()
            adults_value = self.find_element_by_id("group_adults")
            value = adults_value.get_attribute('value')

            if int(value) == 1:
                break

        increase = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase.click()

    def click_search(self):
        self.find_element_by_css_selector(
            'button[type="submit"]'
        ).click()

    def booking_filterations(self):
        filteration = BookingFilterations(driver=self)
        filteration.apply_star_rating(4, 5)
        filteration.price_lowest_first()

    def report_listings(self):
        el = self.find_element_by_id(
            'hotellist_inner'
        )
        report = BookingReport(el)
        table = PrettyTable(
            field_names=['Hotel Name', 'Hotel price', 'Hotel rating'],

        )
        table.add_rows(report.pull_titles())
        print(table)
