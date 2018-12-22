# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:05:02 2018

@author: Dr Nicholas Francis (c)
"""

import requests
from bs4 import BeautifulSoup
import os
import numpy as np

ticker_list = [x.strip() for x in open("F:\\System\\PVWAVE\\Crypto\\tickers.txt", "r").readlines()]

print("Number of tickers: ", len(ticker_list))

for ticker in ticker_list:
    print(ticker)
    if ticker == "bitcoin/btc-usd":
        postData = {
            "curr_id" : "49799",
            "smlID" : "145284",
            "header" : "BTC%2FUSD+Kraken+Historical+Data",
            "st_date" : "06%2F01%2F2016",
            "end_date" : "12%2F22%2F2018",
            "interval_sec" : "Daily",
            "sort_col" : "date",
            "sort_ord" : "DESC"
            }
        urlheader = {
            "Cookie": "adBlockerNewUserDomains=1541437573; optimizelyEndUserId=oeu1541437581960r0.3993521926981858; _ga=GA1.2.1729748745.1541437588; __gads=ID=778152b2f2dc7264:T=1541437590:S=ALNI_MZ-2P3R868IlB4H4wHVmipp9Y2KvQ; __qca=P0-1975209148-1541437600405; G_ENABLED_IDPS=google; cookieConsent=was-set; r_p_s_n=1; _gid=GA1.2.734884496.1545323721; geoC=GB; comment_notification_201938397=1; gtmFired=OK; PHPSESSID=v203k3il5957fpo67bmlj1d8a6; StickySession=id.96673677025.583.www.investing.com; _fbp=fb.1.1545502376288.1959092316; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A5%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A49799%3Bs%3A10%3A%22pair_title%22%3Bs%3A17%3A%22Bitcoin+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A33%3A%22%2Fcrypto%2Fbitcoin%2Fbtc-usd%3Fcid%3D49799%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A997651%3Bs%3A10%3A%22pair_title%22%3Bs%3A18%3A%22Ethereum+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A35%3A%22%2Fcrypto%2Fethereum%2Feth-usd%3Fcid%3D997651%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22945629%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A17%3A%22Bitcoin+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A23%3A%22%2Fcrypto%2Fbitcoin%2Fbtc-usd%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22997650%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A18%3A%22Ethereum+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A24%3A%22%2Fcrypto%2Fethereum%2Feth-usd%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A1010796%3Bs%3A10%3A%22pair_title%22%3Bs%3A17%3A%22Bitcoin+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A35%3A%22%2Fcrypto%2Fbitcoin%2Fbtc-usd%3Fcid%3D1010796%22%3B%7D%7D%7D%7D; UserReactions=true; nyxDorf=Njo%2FbWYuP2I0YW1kYi8xMj9vM3Zkajc2; billboardCounter_1=2; ses_id=NXsxcDE%2BNDxiJjo8ZjdlZz9vP21lYWJoNTcwOjExYnRgdDQ6bjkxd2JtOnQ1NjcrZzM%2BamU6YmE9azA1NWM1YzVkMTAxYTRrYjQ6Y2Y1ZTY%2FOD9tZWpiYTVnMDAxYGI5YGc0ZW49MWViMjoyNTs3Omd1PiJlIWJzPW8wYDV0NXI1OjFwMWI0O2I1OmNmZGViP2o%2FY2VqYjM1YjAwMTRiemAr",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.investing.com",
            "Accept-Encoding": "gzip, deflate, br", 
            "Host": "www.investing.com",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/plain, */*; q=0.01",
            "Referer": "https://www.investing.com/crypto/bitcoin/btc-usd-historical-data?cid=49799",
            "Connection": "keep-alive",
            "Content-Length": "183"
          }
    if ticker == "ethereum/eth-usd":
         postData = {
            "curr_id" : "997651",
            "smlID" : "145284",
            "header" : "ETH%2FUSD+Kraken+Historical+Data",
            "st_date" : "06%2F01%2F2016",
            "end_date" : "12%2F22%2F2018",
            "interval_sec" : "Daily",
            "sort_col" : "date",
            "sort_ord" : "DESC"
            }
         urlheader = {
            "Cookie": "adBlockerNewUserDomains=1541437573; optimizelyEndUserId=oeu1541437581960r0.3993521926981858; _ga=GA1.2.1729748745.1541437588; __gads=ID=778152b2f2dc7264:T=1541437590:S=ALNI_MZ-2P3R868IlB4H4wHVmipp9Y2KvQ; __qca=P0-1975209148-1541437600405; G_ENABLED_IDPS=google; cookieConsent=was-set; r_p_s_n=1; _gid=GA1.2.734884496.1545323721; geoC=GB; comment_notification_201938397=1; gtmFired=OK; PHPSESSID=v203k3il5957fpo67bmlj1d8a6; StickySession=id.96673677025.583.www.investing.com; _fbp=fb.1.1545502376288.1959092316; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A5%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A49799%3Bs%3A10%3A%22pair_title%22%3Bs%3A17%3A%22Bitcoin+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A33%3A%22%2Fcrypto%2Fbitcoin%2Fbtc-usd%3Fcid%3D49799%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A997651%3Bs%3A10%3A%22pair_title%22%3Bs%3A18%3A%22Ethereum+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A35%3A%22%2Fcrypto%2Fethereum%2Feth-usd%3Fcid%3D997651%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22945629%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A17%3A%22Bitcoin+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A23%3A%22%2Fcrypto%2Fbitcoin%2Fbtc-usd%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22997650%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A18%3A%22Ethereum+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A24%3A%22%2Fcrypto%2Fethereum%2Feth-usd%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A1010796%3Bs%3A10%3A%22pair_title%22%3Bs%3A17%3A%22Bitcoin+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A35%3A%22%2Fcrypto%2Fbitcoin%2Fbtc-usd%3Fcid%3D1010796%22%3B%7D%7D%7D%7D; UserReactions=true; nyxDorf=Njo%2FbWYuP2I0YW1kYi8xMj9vM3Zkajc2; billboardCounter_1=2; ses_id=NXsxcDE%2BNDxiJjo8ZjdlZz9vP21lYWJoNTcwOjExYnRgdDQ6bjkxd2JtOnQ1NjcrZzM%2BamU6YmE9azA1NWM1YzVkMTAxYTRrYjQ6Y2Y1ZTY%2FOD9tZWpiYTVnMDAxYGI5YGc0ZW49MWViMjoyNTs3Omd1PiJlIWJzPW8wYDV0NXI1OjFwMWI0O2I1OmNmZGViP2o%2FY2VqYjM1YjAwMTRiemAr",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.investing.com",
            "Accept-Encoding": "gzip, deflate, br", 
            "Host": "www.investing.com",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/plain, */*; q=0.01",
            "Referer": "https://www.investing.com/crypto/bitcoin/btc-usd-historical-data?cid=997651",
            "Connection": "keep-alive",
            "Content-Length": "183"
          }
    url = 'https://www.investing.com/instruments/HistoricalDataAjax'
    req = requests.post(url, headers=urlheader, data=postData)
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
