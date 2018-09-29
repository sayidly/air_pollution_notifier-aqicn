# -*- coding: utf-8 -*-

import json
from getStationAQI import stationAQI
import asyncio

with open('config.json') as config:
    config_json = json.load(config)

with open('info.json') as info:
    info_json = json.load(info)

sh = stationAQI(config_json['stationCode'], config_json['aqicnToken'])
s = asyncio.run(sh.getStationJSON(config_json['stationCode'], config_json['aqicnToken']))

print(s)