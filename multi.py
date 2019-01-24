import requests
import json
from password.password import *
import binascii

headers = {'apikey':MULTIAPIKEY}

# ※注意※これはスタブプログラムです。

payload = {'method':'getmultibalances','params':['*','MKICoins']}
response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

# response_multi1はrequestsのオブジェクトで、requests.json()ということ。
# pythonの辞書型にデコードされる。
data_multi1 = response_multi1.json()
#print(data_multi1)

payload = {'method':'liststreamkeyitems','params':['accountname','1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s']}
response_multi2 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)
data_multi2 = response_multi2.json()
data = data_multi2["result"][0]["data"]
accountname = binascii.unhexlify(data).decode('utf-8')

accountname_1 = accountname
address_1 = "1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s"
qty_1 = data_multi1["result"]["1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s"][0]["qty"]

# 2件目

payload = {'method':'liststreamkeyitems','params':['accountname','1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA']}
response_multi2 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)
data_multi2 = response_multi2.json()
data = data_multi2["result"][0]["data"]
accountname = binascii.unhexlify(data).decode('utf-8')

accountname_2 = accountname
address_2 = "1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA"
qty_2 = data_multi1["result"]["1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA"][0]["qty"]

# 3件目

payload = {'method':'liststreamkeyitems','params':['accountname','163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV']}
response_multi2 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)
data_multi2 = response_multi2.json()
data = data_multi2["result"][0]["data"]
accountname = binascii.unhexlify(data).decode('utf-8')

accountname_3 = accountname
address_3 = "163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV"
qty_3 = data_multi1["result"]["163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV"][0]["qty"]

print(accountname_1)
print(address_1)
print(qty_1)
print(accountname_2)
print(address_2)
print(qty_2)
print(accountname_3)
print(address_3)
print(qty_3)




return json.dumps(testdata)