import requests

token = '2d20b5f834a90f9a1af1463bc9114a477f96a50c'
city = 'shanghai'

def getJSON(token, city):
    print(token)
    print(city)
    city_url = 'http://api.waqi.info/search/?'
    parameters = {"token": token, "keyword": city}
    r = requests.get(city_url, params=parameters)
    print(r.json())

getJSON(token, city)
