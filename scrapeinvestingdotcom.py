# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:05:02 2018

@author: Dr Nicholas Francis (c)
"""

import requests
from bs4 import BeautifulSoup
import os
import numpy as np

# BTC scrape https://www.investing.com/crypto/bitcoin/btc-usd-historical-data
# ETH scrape https://www.investing.com/crypto/ethereum/eth-usd-historical-data

ticker_list = [x.strip() for x in open("F:\\System\\PVWAVE\\Crypto\\tickers.txt", "r").readlines()]
urlheader = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

print("Number of tickers: ", len(ticker_list))

for ticker in ticker_list:
    print(ticker)
    url = "https://www.investing.com/crypto/"+ticker+"-historical-data"
    req = requests.get(url, headers=urlheader, data=payload)
    soup = BeautifulSoup(req.content, "lxml")

    table = soup.find('table', id="curr_table")
    split_rows = table.find_all("tr")
    
    newticker=ticker.replace('/','\\')

    output_filename = "F:\\System\\PVWAVE\\Crypto\\{0}.csv".format(newticker)
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    output_file = open(output_filename, 'w')
    header_list = split_rows[0:1]
    split_rows_rev = split_rows[:0:-1]
    
    for row in header_list:
        columns = list(row.stripped_strings)
        columns = [column.replace(',','') for column in columns]
        if len(columns) == 7:
            output_file.write("{0}, {1}, {2}, {3}, {4}, {5}, {6} \n".format(columns[0], columns[2], columns[3], columns[4], columns[1], columns[5], columns[6]))

    for row in split_rows_rev:
        columns = list(row.stripped_strings)
        columns = [column.replace(',','') for column in columns]
        if len(columns) == 7:
            output_file.write("{0}, {1}, {2}, {3}, {4}, {5}, {6} \n".format(columns[0], columns[2], columns[3], columns[4], columns[1], columns[5], columns[6]))

    output_file.close()