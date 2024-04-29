from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.edeka.de/eh/angebote.jsp"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# accept_cookies_btn = driver.find_element(By.ID, "popin_tc_privacy_button").click()

accept_cookies_btn = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "popin_tc_privacy_button"))
)
accept_cookies_btn.click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,".css-6su6cu"))
)

products = driver.find_elements(By.CSS_SELECTOR, '.css-1uiiw0z')

product_detail = []

for product in products:
    try:
        price = product.find_element(By.CSS_SELECTOR, ".css-1tty58m").text
        img = product.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        try:
            name = product.find_element(By.CSS_SELECTOR, ".css-6ha7pe").text
        except Exception as e:
            name = product.find_element(By.CSS_SELECTOR, ".css-ws0zws").text
        product_detail.append({
            "name": name,
            "price": price,
            "image": img
        })
    except Exception as e:
        print("Couldnt extract a product", e)
print(product_detail)
print(len(product_detail))
exit_driver = input("type 'exit' to quit the driver\n")

if exit_driver == "exit":

    driver.close()
    driver.quit()
