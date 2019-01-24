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

for key in data_multi1
  print(key)



