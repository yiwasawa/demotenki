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

