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

try:
    accept_cookies_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "popin_tc_privacy_button"))
    )
    accept_cookies_btn.click()
except Exception as e:
    print("Failed to click on accept cookies button:", e)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1wpdppb"))
    )
    products = driver.find_elements(By.CSS_SELECTOR, ".css-1uiiw0z")

    product_details = []
    for product in products:
        try:
            price = product.find_element(By.CSS_SELECTOR, "span.css-1tty58m").text
            name = product.find_element(By.CSS_SELECTOR, ".css-6ha7pe").text
            img_src = product.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
            product_details.append({
                'name': name,
                'price': price,
                'image': img_src
            })
        except Exception as e:
            print("Error extracting product details:", e)

    print(product_details)
except Exception as e:
    print("Failed to locate products on the page:", e)

exit_driver = input("Type 'exit' to quit the driver: ")
if exit_driver.lower() == "exit":
    driver.close()
    driver.quit()
