import json
import requests

from tqdm import tqdm
from bs4 import BeautifulSoup


# get the source from qcoom
res = requests.get("https://qcoom.com/campaign-motor-bike-accessories")

# write to a file
with open("source.html", "w") as html_file:
    html_file.write(res.text)

# initiate html parser
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.prettify())
products = soup.select(".product-item-info")

data = []

for product in tqdm(products):
    name = product.select_one(".product-item-name a").text.strip()
    regular_price = product.select_one(".old-price .price").text.strip()[4:].replace(",", "")
    offer_price = product.select_one(".special-price .price").text.strip()[4:].replace(",", "")

    data.append({
        "name": name,
        "regular_price": regular_price,
        "offer_price": offer_price,
    })

# print(data)

# write to a file
with open("products.json", "w") as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True)
