from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Categories:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.categories_list = []

    def categories_list(self):
        cat_elements = self.driver.find_element(
            By.ID, "category-menu-group-ab-montag"
        ).find_elements(By.TAG_NAME, "a")
        for cat in cat_elements:
            category = cat.get_attribute("href").split("#")[1]
            self.categories_list.append(category)
        return self.categories_list

