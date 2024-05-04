from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Categories:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cats_list = []
        self.cats_ids = []

    def category_id_finder(self):
        # Finding categories ids to use in categories_list function
        self.cats_ids.clear()
        categories_ids_wrapper = self.driver.find_element(
            By.CSS_SELECTOR, ".carousel-swiper__wrapper"
        ).find_elements(By.CSS_SELECTOR, ".swiper-slide")
        for cat_id in categories_ids_wrapper:
            self.cats_ids.append(cat_id.get_attribute("id"))
        return self.cats_ids

    def categories_ids_list(self, cats_ids):
        self.cats_list.clear()
        for cat_id in cats_ids:
            cat_elements = self.driver.find_element(
                By.ID, cat_id
            ).find_elements(By.TAG_NAME, "a")
            self.cats_list.extend([element.get_attribute("href").split("#")[1] for element in cat_elements])
        return self.cats_list
