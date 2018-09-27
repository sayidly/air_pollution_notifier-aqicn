import requests
import json

token = '2d20b5f834a90f9a1af1463bc9114a477f96a50c'
city = 'shanghai'

def showCityInfo(response):
    for cityNum in range(len(response)):
        print(cityNum+1, response[cityNum]['uid'], response[cityNum]['aqi'], response[cityNum]['station']['name'])


def getInput(response, token):
    inputNum  = input("请输入数字: ")
    print(inputNum)

    try:
        rawNum = int(inputNum)
        number = rawNum - 1
        if number in range(len(response)):
            print('yes')
            print(type(response[number]))
            print(response[number])
        
            stationCode = response[number]['uid']
            print("请在 config.json 文件中，把 stationCode 修改为" + str(stationCode))
            print('使用愉快！')
            
            # write into json file
            with open('data.json', 'w') as outfile:
                json.dump(stationCode, outfile)

        else:
            print('你输入的数字不在列表中')
            getInput(response, token)

    except ValueError:
        print("你输入的不是整数")
        getInput(response, token)

    
    
def getJSON(token, city):
    print(token)
    print(city)
    city_url = 'http://api.waqi.info/search/?'
    parameters = {"token": token, "keyword": city}
    r = requests.get(city_url, params=parameters)
    #print(r.json())
    response_city = r.json()
    #print(response_city['data'])
    print(len(response_city['data']))
    showCityInfo(response_city['data'])
    getInput(response_city['data'], token)


getJSON(token, city)



