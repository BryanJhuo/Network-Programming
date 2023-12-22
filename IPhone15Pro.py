import requests
from bs4 import BeautifulSoup
import json as js


url_1 = "https://www.apple.com/tw/shop/buy-iphone/iphone-15-pro"
request = requests.get(url_1)
html = BeautifulSoup(request.content, "html.parser")
'''
#清單
test1 = html.find_all("span", {"class": "globalnav-link-text"})
#清單json
json_text = html.find("script", {"id": "__ACGH_DATA__", "type": "application/json"})
'''
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
        if int(size) < 10:
            size += "tb"
        else:
            size += "gb"

        if size not in capacities:
            capacities.append(size)

    capacities = sorted(capacities)
    for i in range(1, 3):
        temp = capacities[i]
        capacities[i] = capacities[i + 1]
        capacities[i + 1] = temp
    return capacities

def getDetail(size, capacity, color):   # 擷取型號、價錢、產編
    result = []
    url = "https://www.apple.com/tw/shop/buy-iphone/iphone-15-pro/" + size + "吋顯示器-" + capacity + "-" + color
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