# -*- coding: utf-8 -*-

import StationAQI
import werobot
import re
import json

robot = werobot.WeRoBot(token='mytoken')


@robot.handler
def aqi(*args):
	return json.dumps(StationAQI.getStationJSON(), ensure_ascii= False)

# 让服务器监听在 0.0.0.0:8080
robot.config['HOST'] = '127.0.0.1'
robot.config['PORT'] = 8080

#robot.config["APP_ID"] = "wx1f0f6bbb3392da37"
#robot.config['ENCODING_AES_KEY'] = '0145b463291a78d8a6c03c300fa02c09'

# testing
robot.config["APP_ID"] = "wx07910350914a1994"
robot.config['ENCODING_AES_KEY'] = '7ec65182bd26af5c323c0fa3e4e66c42'


robot.run()