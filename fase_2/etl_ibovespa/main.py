import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
import time

def save_stocks_values():

    url = 'https://www.google.com/finance/markets/most-active'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find('ul', {'class':'sbnBtf'}).find_all('div', {'class':'SxcTic'})

    df = pd.DataFrame()

    for item in items:
        date = datetime.datetime.now()
        symbol = item.find('div', {'class':'iLEcy'}).find('div', {'class':'COaKTb'}).text
        name = item.find('div', {'class':'ZvmM7'}).text
        price = item.find('div', {'class':'YMlKec'}).text
        change = item.find('span', {'class':'P2Luy'}).text

        tmp = pd.DataFrame(
            data = {
                'date':[date],
                'symbol':[symbol],
                'name':[name],
                'price':[price],
                'change':[change]
            }
        )

        df = pd.concat([df, tmp])

    df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d %H:%M:%S')
    # print(df.shape[0])
    filename = str(datetime.datetime.now())[:16].replace(' ', '-').replace(':', '-')
    # print(filename)

    df.to_csv(f'data/file-{filename}.csv')

if __name__ == '__main__':

    while True:
        hora_exec = str(datetime.datetime.now())[:16]
        save_stocks_values()
        print(f"Salvando arquivo {hora_exec} | Horário atual: {str(datetime.datetime.now())[:16]}")
        print()
        time.sleep(60*60)
    