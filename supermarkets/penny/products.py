# Getting details of products from the categories given
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


class Product:
    def __init__(self, driver):
        self.driver = driver
        self.products_list = []

    def product_dictionary(self, item, category_name, date):
        try:
            product_name = item.find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a").text
            try:
                product_price_was = item.find_element(By.CSS_SELECTOR, "span.value").text
            except NoSuchElementException:
                product_price_was = ""
            product_price_now = item.find_element(By.CSS_SELECTOR, "span.bubble__price").text
            image = item.find_element(By.TAG_NAME, "img").get_attribute("src")
            return {
                "category": category_name,
                "product": product_name,
                "old price": product_price_was,
                "new price": product_price_now,
                "image link": image,
                "starting date": date[0],
                "ending date": date[1]
            }
        except NoSuchElementException:
            print("This is probably a teaser")
            return None

    def get_offers_date(self, category):
        current_year = datetime.now().year

        date_wrapper = self.driver.find_element(By.CSS_SELECTOR, ".category-menu")
        date_element = date_wrapper.find_element(By.CSS_SELECTOR, ".active")
        offer_dates = date_element.get_attribute("data-startend")
        start_day_string = f'{offer_dates.split(" - ")[0].replace(".", "/")}{current_year}'
        start_day = datetime.strptime(start_day_string, "%d/%m/%Y")
        end_day = start_day + timedelta(days=5)

        if "ab-montag" in category:
            return [start_day, end_day]
        elif "ab-donnerstag" in category:
            return [start_day + timedelta(days=3), end_day]
        elif "ab-freitag" in category:
            return [start_day + timedelta(days=4), end_day]
        elif "naechsten-montag" in category:
            return [start_day, end_day]
        elif "ab-naechsten-mittwoch" in category:
            return [start_day + timedelta(days=3), end_day]
        elif "ab-naechsten-freitag" in category:
            return [start_day + timedelta(days=4), end_day]

    def products_data_export(self, all_categories):
        self.products_list.clear()
        for category_name in all_categories:
            cat_section = self.driver.find_element(By.ID, category_name)
            cat_list = cat_section.find_elements(By.TAG_NAME, "li")
            self.driver.execute_script("arguments[0].scrollIntoView(true)", cat_section)
            date_list = self.get_offers_date(category_name)
            cat_name = category_name.replace("-", " ")
            for item in cat_list:
                product_info = self.product_dictionary(item, cat_name, date_list)
                if product_info:
                    self.products_list.append(product_info)
        return self.products_list
