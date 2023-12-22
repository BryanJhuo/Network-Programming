import requests
from bs4 import BeautifulSoup
import json as js

url_1 = "https://www.apple.com/tw/shop/buy-iphone/iphone-15"
request = requests.get(url_1)
html = BeautifulSoup(request.content, "html.parser")

def getColor():     # 擷取顏色
    colors = []
    allColors = html.find("div", {"class": "product-selection-area noscript as-l-container"}).find(
        "div").find_all("span", {"class": "dimensionColor"})
    for single_color in allColors:
        if single_color.contents[0] not in colors:
            colors.append(single_color.contents[0])
    return colors

def getCapacity():    # 擷取容量
    capacities = []
    allCapacity = html.find("div", {"class": "product-selection-area noscript as-l-container"}).find(
        "div").find_all("span", {"class": "dimensionCapacity"})

    for single_capacity in allCapacity:
        size = single_capacity.contents[0]
        size += "gb"

        if size not in capacities:
            capacities.append(size)

    capacities = sorted(capacities)
    return capacities

def getDetail(size, capacity, color):   # 擷取型號、價錢、產編
    result = []
    url = "https://www.apple.com/tw/shop/buy-iphone/iphone-15/" + size + "吋顯示器-" + capacity + "-" + color
    req = requests.get(url)
    bsObj = BeautifulSoup(req.content, "html.parser")
    detail = bsObj.find("script", {"type": "application/ld+json"})
    detailJson = js.loads(detail.get_text())
    result.append(detailJson['name'])
    result.append(detailJson['offers'][0]['priceCurrency'] + " " + str(detailJson['offers'][0]['price']))
    result.append(detailJson['offers'][0]['sku'])
    return result

def getPickUp(type):    # 擷取取貨資訊
    results = []
    url = ("https://www.apple.com/tw/shop/fulfillment-messages?little=false&parts.0=" + type + "&mts.0=regular&mts.1=sticky&fts=true")
    req = requests.get(url)
    bsObj = BeautifulSoup(req.content, "html.parser")
    data_jason = js.loads(bsObj.get_text())
    data = data_jason['body']['content']['pickupMessage']['stores'][0]
    canPickup = data['partsAvailability'][type]['storePickEligible']
    results.append(canPickup)
    if (canPickup):
        # 新增店名
        results.append(data['storeName'])
        # 新增可以取貨的時間
        results.append(data['partsAvailability'][type]['pickupSearchQuote'])
        # 新增可以取貨方式
        results.append(data['partsAvailability'][type]['pickupType'])
    else:
        results.append("Can't pick up.")
    return results