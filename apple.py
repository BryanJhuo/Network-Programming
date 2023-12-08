import requests
from bs4 import BeautifulSoup


url = "https://www.apple.com/tw"
url_1 = "https://www.apple.com/tw/shop/buy-iphone/iphone-15-pro"
request = requests.get(url_1)
html = BeautifulSoup(request.content, "html.parser")
'''
#清單
test1 = html.find_all("span", {"class": "globalnav-link-text"})
#清單json
json_text = html.find("script", {"id": "__ACGH_DATA__", "type": "application/json"})
'''

#擷取顏色
colors = []
allColors = html.find("div", {"class": "product-selection-area noscript as-l-container"}).find(
    "div").find_all("span", {"class": "dimensionColor"})
for single_color in allColors:
    if single_color.contents[0] not in colors:
        colors.append(single_color.contents[0])

#擷取容量
capacities = []
allCapacity = html.find("div", {"class": "product-selection-area noscript as-l-container"}).find(
    "div").find_all("span", {"class": "dimensionCapacity"})

for single_capacity in allCapacity:
    size = single_capacity.contents[0]
    if int(size) < 10:
        size += "TB"
    else:
        size += "GB"

    if size not in capacities:
        capacities.append(size)

capacities = sorted(capacities)
for i in range(1, 3):
    temp = capacities[i]
    capacities[i] = capacities[i + 1]
    capacities[i + 1] = temp

print(capacities)
