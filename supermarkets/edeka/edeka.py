from datetime import datetime
import csv
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

offer_date_string = driver.find_element(By.CSS_SELECTOR, ".css-1skty0g")
dates = [date.strip().replace(".", "")for date in offer_date_string.text.split("vom")[1].split("bis zum")]

starting_date = datetime.strptime(dates[0], "%d%m%Y").date()
ending_date = datetime.strptime(dates[1], "%d%m%Y").date()

filename = f"edeka_{starting_date}_to_{ending_date}"
print(filename)


products = driver.find_elements(By.CSS_SELECTOR, '.css-1uiiw0z')

product_detail = []

for product in products:
    try:
        price = product.find_element(By.CSS_SELECTOR, ".css-1tty58m").text
        img = product.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        try:
            name = product.find_element(By.CSS_SELECTOR, ".css-6ha7pe").text
        except:
            name = product.find_element(By.CSS_SELECTOR, ".css-ws0zws").text
        product_detail.append({
            "name": name,
            "price": price,
            "image": img
        })
    except Exception as e:
        print("Couldnt extract a product", e)

current_date = datetime.now().strftime("%d-%m-%Y")
filename = f"edeka_products_{current_date}.csv"

csv_path = "E:/Coding/VSCode/SumOFF/csv_files/edeka"

with open(f"{csv_path}/{filename}", "w", newline="") as file:
    fieldnames = ["name", "price", "image"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in product_detail:
        writer.writerow(row)

exit_driver = input("type 'exit' to quit the driver\n")

if exit_driver == "exit":
    try:
        driver.close()
    finally:
        driver.quit()
