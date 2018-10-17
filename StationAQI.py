# -*- coding: utf-8 -*-

import os
import requests
import json

with open('config.json') as config:
    config_json = json.load(config)

with open('info.json') as info:
    info_json = json.load(info)


def getStationJSON():
    idx = config_json['stationCode']
    token = config_json['aqicnToken']
    print(idx)
    print(token)
    station_URL = "http://api.waqi.info/feed/@%(idx)s/?token=%(token)s" % {
        'idx': idx, 'token': token}
    print(station_URL)
    response_city = getData(station_URL)
    print(response_city)
    result = processData(response_city)
    return result
    # print(result)
    # await self.prepareContent(result)


def getData(url):
    try:
        response = requests.get(url)
        response_Station = response.json()
        # print(response_Station['data'])
        return response_Station
    except error:
        print(error)


def processData(response):
    data = response["data"]
    result = {}
    result['station'] = data['city']['name']
    result['aqi'] = data['aqi']
    result['time'] = data['time']['s']
    result['iaqi'] = data['iaqi']
    print(result)

    def calculateLevel(aqi):
        level = 0
        if aqi >= 0 and aqi <= 50:
            level = 1
        elif aqi >= 51 and aqi <= 100:
            level = 2
        elif aqi >= 101 and aqi <= 150:
            level = 3
        elif aqi >= 151 and aqi <= 200:
            level = 4
        elif aqi >= 201 and aqi <= 300:
            level = 5
        elif aqi > 300:
            level = 6
        return level

    level = calculateLevel(result['aqi'])
    print(level)

    def selectInfoText(level):
        if level > 6 or level < 0:
            level = 0
        levelInfo = {}
        levelInfo['value'] = level
        levelInfo['name'] = info_json['level'][level]['name']
        levelInfo['implication'] = info_json['level'][level]['implication']
        levelInfo['statement'] = info_json['level'][level]['statement']
        return levelInfo

    levelInfo = selectInfoText(level)
    result['level'] = levelInfo
    print(result)
    return result
