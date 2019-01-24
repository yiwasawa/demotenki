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

for key in data_multi1:
  print(key)

for value in data_multi1.values():
  print(value)

for key in data_multi1["result"]:
  print(key)

data_multi2 = data_multi1["result"]
print(data_multi2)

for i in data_multi2:
    print(data_multi2[i].name)
    print(data_multi2[i].qty)
