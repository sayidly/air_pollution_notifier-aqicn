# -*- coding: utf-8 -*-

import StationAQI
import werobot
import re
import json

robot = werobot.WeRoBot(token='mytoken')


@robot.handler
def aqi(*args):
    return json.dumps(StationAQI.getStationJSON(), ensure_ascii=False)


# 让服务器监听在 0.0.0.0:8080
robot.config['HOST'] = '127.0.0.1'
robot.config['PORT'] = 8080


# robot.config["APP_ID"] = "wx1f0f6bbb3392da37"
# robot.config['APP_SECRET'] = '0145b463291a78d8a6c03c300fa02c09'

# testing
robot.config["APP_ID"] = "wx07910350914a1994"
robot.config['APP_SECRET'] = '7ec65182bd26af5c323c0fa3e4e66c42'

# 自定义菜单
client = robot.client
client.create_menu({
    "button": [{
        "type": "click",
        "name": "今日歌曲",
        "key": "music"
    }]
})


@robot.key_click("music")
def music(message):
    return '你点击了“今日歌曲”按钮'


robot.run()
