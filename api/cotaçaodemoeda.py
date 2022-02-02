import requests
import json 


cot = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cot =  cot.json()
cot_euro  =  cot['EURBRL']["bid"]
'''print(cot)
'''
print(cot_euro)