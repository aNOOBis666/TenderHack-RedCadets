import requests
import json
import time

url_list = []


def find_urls():
    for page in range(1):
        url = "https://old.zakupki.mos.ru/api/Cssp/Purchase/Query?queryDto=%7B%22filter%22%3A%7B%22typeIn%22%3A%5B1" \
               "%5D%2C%22regionPaths%22%3A%5B%22.1.504.%22%5D%2C%22auctionSpecificFilter%22%3A%7B%22stateIdIn%22%3A" \
               "%5B19000004%5D%7D%2C%22needSpecificFilter%22%3A%7B%7D%2C%22tenderSpecificFilter%22%3A%7B%7D%7D%2C" \
               "%22order%22%3A%5B%7B%22field%22%3A%22relevance%22%2C%22desc%22%3Atrue%7D%5D%2C%22withCount%22%3Atrue" \
               "%2C%22take%22%3A10%2C%22skip%22%3A{page_number}0%7D ".format(page_number=page)
        response = requests.get(url)
        web_page = response.text
        json_str = json.loads(web_page)
        for i in json_str["items"]:
            url_list.append(i["auctionId"])
        time.sleep(1)


def get_current_page(page):
    num_list = []
    dateTime = []
    bets = []
    url = "https://zakupki.mos.ru/newapi/api/Auction/Get?auctionId={page}".format(page=page)
    response = requests.get(url)
    web_page = response.text
    json_str = json.loads(web_page)
    for i in json_str["bets"]:
        num_list.append(i["num"])
        dateTime.append(i["cost"])
        bets.append(i["serverTime"])
    time.sleep(2)


if __name__ == '__main__':
    find_urls()
    for url in url_list:
        get_current_page(url)
