from selenium.webdriver.remote.webdriver import WebDriver


class BookingFilterations:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        rating_element = self.driver.find_element_by_id("filter_class")
        star_child_elements = rating_element.find_elements_by_css_selector("*")

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def price_lowest_first(self):
        self.driver.find_element_by_css_selector(
            'a[data-type="price"]'
        ).click()
