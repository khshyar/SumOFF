import constants as c
import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from categories_finder import Categories
from products import Product
options = Options()
options.add_experimental_option("detach", True)


class Penny(webdriver.Chrome):
    def __init__(self, driver_path="C:/Projects/SumOFF/SeleniumDrivers/124063"):
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Penny, self).__init__(options=options)
        self.implicitly_wait(0.01)

    def landing_page(self):
        self.get(c.URL)

    def accept_cookies(self):
        # find the shadow wrapper first
        shadow_wrapper = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, 'usercentrics-root'))
        )
        shadow_root = shadow_wrapper.shadow_root
        cookies_accept = WebDriverWait(shadow_root, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]'))
        )
        cookies_accept.click()



    def get_offers_categories(self):
        categories = Categories(driver=self)
        cat_ids = categories.category_id_finder()
        cat_ids_list = categories.categories_ids_list(cat_ids)
        return cat_ids_list

    def get_products_details(self, category):
        products = Product(driver=self)
        return products.products_data_export(category)


if __name__ == "__main__":
    ins = Penny()
    ins.landing_page()
    ins.accept_cookies()
    categories_list = ins.get_offers_categories()
    print(ins.get_products_details(categories_list))
