import os
import sys

sys.path.append('/home/ec2-user/.pyenv/versions/3.6.2/lib/python3.6/site-packages')

from bottle import *
import pyodbc
from password.password import *
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

import subprocess
import json
import datetime
import requests
import binascii

print("test")

wk_time = datetime.datetime.fromtimestamp(1554432807)

wk_time = wk_time + datetime.timedelta(hours=9)

print(wk_time)

conv_time = datetime.datetime.fromtimestamp(wk_time).strftime("%Y/%m/%d %H:%M:%S")

print(conv_time)