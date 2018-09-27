import os
import time
import datetime
import json
import requests
import asyncio

with open('config.json') as config:
    config_json = json.load(config)

print(config_json)

print(config_json["city"])

def switch_time_zone():
    """
    切换时区到settings.TIME_ZONE
    """
    #os.environ['TZ'] = 'US/Eastern'
    os.environ["TZ"] = "Asia/Shanghai"
    time.tzset()
    return datetime.datetime.now()

async def getStationJSON():
    idx = config_json["stationCode"]
    token = config_json["aqicnToken"]
    print(idx)
    print(token)
    station_URL = 'http://api.waqi.info/feed/@%(idx)s/?token=%(token)s' % {'idx': idx, 'token': token}
    print(station_URL)
    response_city = await getData(station_URL)
    print(response_city)
    #result = await self.processData(response_city)
    #print(result)
    #await self.prepareContent(result)

async def getData(url):
    try:
        response = requests.get(url)
        response_Station = response.json()
        print(response_Station['data'])
        return response_Station['data']
    except error:
        print(error)

def processData(response):
    data = response.data

print(switch_time_zone())
asyncio.run(getStationJSON())
