import requests
import json
import time
import pandas as pd
import os
import csv
import shutil

url_list = []


def find_urls():
    for page in range(5):
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
    date = []
    times = []
    bets = []
    url = "https://zakupki.mos.ru/newapi/api/Auction/Get?auctionId={page}".format(page=page)
    response = requests.get(url)
    web_page = response.text
    json_str = json.loads(web_page)
    try:
        for i in json_str["bets"]:
            datetimelist = i["serverTime"].split()
            times.append(datetimelist[0])
            date.append(datetimelist[1])
            bets.append(i["cost"])
        times.sleep(1)
    except:
        pass
    finally:
        return times, date, bets

def to_dataframe(date, time, bets):
    df = pd.DataFrame({'Дата': date, 'Время': time, 'Ставка': bets})
    # print(df)
    return df

if __name__ == '__main__':
    dict = {}
    find_urls()
    if os.path.isdir('./csvs'):
        shutil.rmtree("csvs")
        os.mkdir("csvs")
    else:
        os.mkdir("csvs")
    for url in url_list:
        date, times, bets = get_current_page(url)
        dict[url] = to_dataframe(date, times, bets)
    for key in dict.keys():          
        data_i = dict[key]
        if len(data_i) >= 5:
            data_i.to_csv(os.path.join('csvs', str(key) + '.csv'))
        
