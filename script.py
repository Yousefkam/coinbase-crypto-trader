from coinbase.wallet.client import Client
from time import sleep
import csv
import datetime
import threading

#https://developers.coinbase.com/docs/wallet/guides/buy-sell

#initializing
print('Welcome to Coinbase Trading bot! By: @usef._.k on instagram')
print('\n')
api_key = input('Enter API Key: ')
api_secret = input('Enter API Secret: ')


#Setting up coinbase client
client = Client(api_key, api_secret)
payment_method = client.get_payment_methods()[0] #USED TO GRAB PAYMENT ID TO ACTUALLY MAKE THE PURCHASE
account = client.get_primary_account()

#Take user input
sell_threshold = float(input("Enter sell threshold (USD): "))
buy_threshold = float(input("Enter buy threshold (USD): "))
crypto = str(input('Enter desired crypto (ETH/BTC): '))
currency_code = 'USD'
amount = float(input('How much do you want to sell/buy from the listed crypto? ex: .23333 bitcoin: '))

buy_price  = client.get_buy_price(currency='USD')
sell_price = client.get_sell_price(currency='USD')

def buying():
    while(True):
        if buy_price <= buy_threshold:
            try:
                account.buy(amount=amount, currency=crypto, payment_method=payment_method.id)
                with open('logs.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([datetime.datetime.now(), crypto, 'buy', amount])
            except:
                pass
        else: pass             

    sleep(600)

def selling():
    while True:
        if sell_price >= sell_threshold:
            try:
                account.sell(amount=amount, currency=crypto, payment_method=payment_method.id)
                with open('logs.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([datetime.datetime.now(), crypto, 'buy', amount])
            except:
                pass   
        else:
            pass    
    sleep(120)


buyThread = threading.Thread(target=buying)
buyThread.start()

sellThread = threading.Thread(target=selling)
sellThread.start()
