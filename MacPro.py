import requests
from bs4 import BeautifulSoup
import json as js

keyboardID = "TA065-CDKG"

def getDetail(state):
    results = []
    url = "https://www.apple.com/tw/shop/fulfillment-messages?little=false&parts.0=Z171&option.0="+state[0]+","+state[1]+","+state[2]+","+state[3]+","+state[4]+","+keyboardID+","+state[5]+","+state[6]+"&mts.0=regular&fts=true"
    req = requests.get(url)
    bsObj = BeautifulSoup(req.content, "html.parser")
    dataJson = js.loads(bsObj.get_text())
    data = dataJson['body']['content']['pickupMessage']['stores'][0]
    results.append(data['storeName'])
    results.append(data['partsAvailability']["Z171"]['pickupSearchQuote'])
    return results

def getPrice(state):
    url ="https://www.apple.com/tw/shop/configUpdate/Z171?node=home%2Fshop_mac%2Ffamily%2Fmac_pro%2Fconfig&option.processor_and_graphics_aos_phantom_z171="+state[0]+"&option.memory_aos_phantom_z171="+state[1]+"&option.hard_drivesolid_state_drive_z171="+state[2]+"&option.chassis_support_z171="+state[3]+"&option.mouse_and_trackpad_z171="+state[4]+"&option.collapsible_keyboard_and_documentation_z171="+keyboardID+"&option.sw_final_cut_pro_z171="+state[5]+"&option.sw_logic_pro_z171="+state[6]+"&bfil=0"
    req = requests.get(url)
    bsObj = BeautifulSoup(req.content, "html.parser")
    priceJson = js.loads(bsObj.get_text())
    data = priceJson['body']['replace']['summary']['prices']['total']
    return data

