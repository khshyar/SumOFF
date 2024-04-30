from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Konfiguration für ChromeOptions
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialisieren des Chrome Webdrivers
driver = webdriver.Chrome(options=chrome_options)

# Webseite laden
driver.get("https://www.rewe.de/angebote/nationale-angebote/?week=current")
time.sleep(5)  # Warten, damit die Webseite vollständig geladen wird

# Extract the date range from the Tab Button
date_range_element = driver.find_element(
    By.CSS_SELECTOR, ".sos-week-tabs__tab-subtitle")
date_range_text = date_range_element.text  # E.g., "29.4. bis 5.5."
date_parts = date_range_text.split(' bis ')
current_year = datetime.now().year

# Correct parsing of the dates with the current year
price_valid_from = datetime.strptime(
    f"{date_parts[0]}{current_year}", "%d.%m.%Y").strftime("%d.%m.%Y")
price_valid_until = datetime.strptime(
    f"{date_parts[1]}{current_year}", "%d.%m.%Y").strftime("%d.%m.%Y")

# Extraktion des Kategorienamens
category_element = driver.find_element(
    By.CSS_SELECTOR, "#sos-title-topangebote-current-week")
# Hier wird der Kategorienname ausgelesen
category_name = category_element.text.strip()

# Suche nach dem übergeordneten Element, das alle Angebote enthält
current_offers = driver.find_elements(
    By.XPATH, '//div[@id="sos-category__grid-topangebote"]//article[@class="cor-offer-renderer-tile cor-link"]')

# Dictionary, um alle Produkte und deren Preise zu speichern
product_details = {}

# Extraktion der Produktnamen und Preise
for offer in current_offers:
    product_name = offer.find_element(
        By.CSS_SELECTOR, '.cor-offer-information__title-link').text.strip()
    price = offer.find_element(
        By.CSS_SELECTOR, '.cor-offer-price__tag-price').text.strip()
    image_url = offer.find_element(
        By.CSS_SELECTOR, '.tkr-lazy').get_attribute('src')

    if product_name:  # Stelle sicher, dass der Produktname nicht leer ist
        product_details[product_name] = {
            'price': price,
            'image_url': image_url,
            'price_valid_from': price_valid_from,
            'price_valid_until': price_valid_until,
            'category': category_name  # Hinzufügen der gelesenen Kategorie
        }

current_date = datetime.now().strftime("%d-%m-%Y")
filename = f"rewe_products_{current_date}.csv"

csv_path = "E:/Coding/VSCode/SumOFF/csv_files/rewe"

# CSV-Datei schreiben
with open(f"{csv_path}/{filename}", 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['product_name', 'price', 'image_url',
                  'price_valid_from', 'price_valid_until', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for product, details in product_details.items():
        writer.writerow({'product_name': product, 'price': details['price'], 'image_url': details['image_url'],
                        'price_valid_from': details['price_valid_from'], 'price_valid_until': details['price_valid_until'], 'category': details['category']})

# Ausgabe des Dictionaries mit Produktnamen und Preisen
print(product_details)

# Warten auf Benutzereingabe, um das Programm zu beenden
input("Press Enter to quit...")

# Schließen des Browsers
driver.quit()
# driver.close()


# from bs4 import BeautifulSoup
# import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# response = requests.get("https://www.rewe.de/angebote/nationale-angebote/?week=current", headers=headers)
# rewe_web_offer = response.text

# print(response)

# html = BeautifulSoup(rewe_web_offer,'html.parser')

# categories = html.find(name="div", class_="sos-categories")
# top_offers_sections = categories.find(name="section", class_="sos-category sos-category--topangebote")
# first_top_offers_section = top_offers_sections.find(name="article", class_="cor-offer-renderer-tile cor-link")

# print(first_top_offers_section)
