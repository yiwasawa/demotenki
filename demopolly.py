from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess

session = Session(region_name="ap-northeast-1")
polly = session.client("polly")

try:
    response = polly.synthesize_speech(Text="ただいまの南さいたまの気温は9.6℃、湿度は48.0％くらいです。", OutputFormat="mp3", VoiceId="Mizuki")
except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)
if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = "/var/www/html/speech.mp3"
        try:
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            print(error)
            sys.exit(-1)
        print("synthesize_speech OK ->>" + output)
else:
    print("Could not stream audio")
    sys.exit(-1)
