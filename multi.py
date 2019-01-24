import requests
import json
from password.password import *



headers = {'apikey':MULTIAPIKEY}
payload = {'method':'getmultibalances','params':['*','MKICoins']}
response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

# response_multi1はrequestsのオブジェクトで、requests.json()ということ。
# pythonの辞書型にデコードされる。
data_multi1 = response_multi1.json()
print(data_multi1)

print("その1")
print(data_multi1["result"])
print("その2")
print(data_multi1["result"]["1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s"])
print("その3")

print(data_multi1["result"]["1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s"][0]["qty"])
print(data_multi1["result"]["1TgN4QggTGgyN8hPcda5qQPA5t2kjj9zXpxMhA"][0]["qty"])
print(data_multi1["result"]["163bVJBXpwrBZX3qsv8aBf4S2KJHaQiPCj2zAV"][0]["qty"])

for key in data_multi1:
  print(key)

for value in data_multi1.values():
  print(value)

for key in data_multi1["result"]:
  print(key)


