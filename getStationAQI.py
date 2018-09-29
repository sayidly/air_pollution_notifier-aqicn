# -*- coding: utf-8 -*-

import os
import requests
import asyncio

class stationAQI:

    def __init__(self, stationCode='1437',aqicnToken='2d20b5f834a90f9a1af1463bc9114a477f96a50c'):
        self.__stationCode = stationCode
        self.__aqicnToken = aqicnToken


    async def getStationJSON(self, idx, token):
        print(idx)
        print(token)
        station_URL = "http://api.waqi.info/feed/@%(idx)s/?token=%(token)s" % {'idx': idx, 'token': token}
        print(station_URL)
        response_city = await getData(station_URL)
        print(response_city)
        result = await processData(response_city)
        #print(result)
        #await self.prepareContent(result)

    async def getData(self, url):
        try:
            response = requests.get(url)
            response_Station = response.json()
            #print(response_Station['data'])
            return response_Station
        except error:
            print(error)

    async def processData(self, response):
        data = response["data"]
        result = {}
        result['station'] = data['city']['name']
        result['aqi'] = data['aqi']
        result['time'] = data['time']['s']
        result['iaqi'] = data['iaqi']
        print(result)
        level = calculateLevel(result['aqi'])
        print(level)
        levelInfo = selectInfoText(level)
        result['level'] = levelInfo
        print(result)
        return result

    def calculateLevel(self, aqi):
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

    def selectInfoText(self, level):
        if level > 6 or level < 0:
            level = 0
        levelInfo = {}
        levelInfo['value'] = level
        levelInfo['name'] = info_json['level'][level]['name'] 
        levelInfo['implication'] = info_json['level'][level]['implication'] 
        levelInfo['statement'] = info_json['level'][level]['statement'] 
        return levelInfo
