from bs4 import BeautifulSoup
import requests   
header = {     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }  
response = requests.get(url="https://www.edeka.de/eh/angebote.jsp", headers=header) 
print(response) 
web_html = response.text  
soup = BeautifulSoup(web_html, "html.parser") 
#print(soup) 
base_category = soup.find("span", class_="css-1tty58m")  
# items = soup.find(class_="css-79elbk") 
# new_item = items.find(class_="css-1wq430v") 
print(base_category)