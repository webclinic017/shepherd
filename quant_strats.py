from colorama import Fore

import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import lxml
import random 
import json 

creds = json.load(open('api.json',))

api = tradeapi.REST(
    creds["apiKeyID"],
    creds["secretKey"],
    creds["endpoint"], api_version='v2'
)

pd.set_option('display.max_rows', 50)

# long-only price momentum strategy based on top 10% performing stocks in S&P 500 based on cumulative return
def price_momentum_cr():
    df = pd.DataFrame()
    yahoo_url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1474675200&period2=1632268800&interval=1d&events=history&includeAdjustedClose=true'
    sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    sp500_list = np.array(sp500[0]['Symbol'])

    for ticker in sp500_list:
        if "." in ticker:
            ticker = ticker.replace(".","-")
        url = yahoo_url.format(ticker)
        df_tmp = pd.read_csv(url)
        df_tmp['Ticker'] = ticker 
        df = pd.concat([df, df_tmp])

    df = df[['Date', 'Ticker', 'Adj Close']]
    df.columns = ['date', 'ticker', 'price']

    df1 = df.pivot_table(index=['date'], columns='ticker', values=['price'])
    # flatten columns multi-index, `date` will become the dataframe index
    df1.columns = [col[1] for col in df1.columns.values]
    
    # compute cumulative returns from prices
    cum_return = (df1.iloc[-1] - df1.iloc[0]) / df1.iloc[0]
    cum_return_percentage = cum_return * 100

    print(Fore.GREEN + "[+] cumulative returns calculated..." + Fore.RESET)

    print(Fore.GREEN + "[+] top 10" + '%' + " stocks based on 5 yr cumulative returns calculated" + Fore.RESET)
    top10 = cum_return_percentage.nlargest(50, 'first')
    client_id = str(random.randint(1,10000000))

    buy_orders = [print(i) for i in top10[1]]
    print("[+] all long positions opened based on cumulative returns...")
    print("[+] long-only price-momentum strategy completed")








