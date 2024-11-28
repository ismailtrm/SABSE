import websocket ,json,pprint,numpy
from binance.client import Client
from binance.enums import *
import time

api_key = "a3411F8a0ce0980a17441D37549c378BoFXeX4CWwR22tkHkzCgD6oUXyZrnYEf6"
api_secret = "59a109fD39430F0Aea144ca4d4416bFDwOpcIqcDCHHPF8Rcf7Ro3R87F5Do1A1a"
analyzed_name = []
my_wallet = []
client = Client(api_key,api_secret)



def get_balance_spot():
    try:
        balances = client.get_account()['balances']
        for balance in balances:
            if float(balance['free']) > 0:
                my_wallet.append((balance['asset'], float(balance['free'])))
        return True
    except Exception as e:
        print(f"Error getting balance: {e}")
        return False
    time.sleep(1)
def decision_analyze():
    i = 0
    global analyzed_name
    global my_wallet
    if len(my_wallet) == 0:
        print("No balance in spot wallet. Skipping analysis.")
        return
    for balance in my_wallet:
        if balance[0] == analyzed_name[i][0]:
            print(f"You have {balance[0]}")
            
            ##alınacak karar
        



        


    


