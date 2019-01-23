import requests
import time
import json
import datetime
import pyodbc
from password.password import *

headers = {'apikey':MULTIAPIKEY}
payload = {'method':'getaddressbalances','params':['1PN6wchQ348Rn8rW5qgbgQZAytZeSuuF8oyT3s']}
response_multi1 = requests.post(MULTIENDPOINT, data=json.dumps(payload), headers=headers)

data_multi1 = response_multi1.json()
print(data_multi1)


qty = json.dumps(data_multi1["result"][0]["qty"])

print(qty)





