from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get("https://www.rewe.de/angebote/nationale-angebote/?week=current", headers=headers)
rewe_web_offer = response.text

html = BeautifulSoup(rewe_web_offer,'html.parser')

categories = html.find(name="div", class_="sos-categories")

top_offers_sections = categories.find(name="section", class_="sos-category sos-category--topangebote")

print(top_offers_sections)