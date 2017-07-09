# This Python file uses the following encoding: utf-8
"""
Obtain today's and tomorrow's forecast from Livedoor
"""

import urllib.request
import json


def readable(text):
    """
    Replace given text so that openJtalk can read it
    """
    text = text.replace("梅雨", "ばいう")
    return text


def parseforecast(data):
    """
    forecast dict を与えるとコンソール出力用にパースします。
    """

    def gettemp(temp, key):
        """
        temp dict から気温をパースします。\n
        最高("max")/最低("min")は key に string で与えます。
        最低気温が null の場合、なにも出力しません。
        """
        return "\ntemp" + key + " " + (temp["temperature"][key]["celsius"]
                                       if temp["temperature"][key] != None else
                                       "")

    return "date " + data["date"] + "\ntelop " + data["telop"] + gettemp(
        data, "min") + gettemp(data, "max")


responce = urllib.request.urlopen(
    'http://weather.livedoor.com/forecast/webservice/json/v1?city=340010')
if responce.code == 200:
    dic = json.loads(responce.read().decode("utf-8"))

    print("forecastat " + dic["publicTime"])

    print("today")
    print(parseforecast(dic["forecasts"][0]))

    print("tomorrow")
    print(parseforecast(dic["forecasts"][1]))

    print("description " + dic["description"]["text"].replace(
        "\n", "").replace(" ", ""))
else:
    print("天気を取得できませんでした")
