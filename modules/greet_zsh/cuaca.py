import requests, datetime
from bs4 import BeautifulSoup

WEATHER_CODE = {
    0: "Cerah",
    1: "Cerah Berawan",
    2: "Cerah Berawan",
    3: "Berawan",
    4: "Berawan Tebal",
    5: "Udara Kabur",
    10: "Asap",
    45: "Kabut",
    60: "Hujan Ringan",
    61: "Hujan Sedang",
    63: "Hujan Lebat",
    80: "Hujan Lokal",
    95: "Hujan Petir",
    97: "Hujan Petir"
}

# UTC0_TO_PERIOD = {
#     0: "Pagi",
#     6: "Siang",
#     12: "Malam"
# }


def weather():
    try:
        response = requests.get("https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-SulawesiSelatan.xml", timeout=0.5)
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        return "..."
    else:
        codes = get_weather_key(response)
        if 0 <= datetime.datetime.now().hour <= 14:
            return ", cuaca hari ini "+ get_weather(codes[0])
        elif 14 < datetime.datetime.now().hour <= 20:
            return ", cuaca hari ini "+ get_weather(codes[1])
        else:
            return ", cuaca hari ini "+ get_weather(codes[2])


def get_weather_key(response):
    soup = BeautifulSoup(response.content, "xml")
    city = soup.find(description="Makassar")
    weather = city.find(description="Weather")
    hours = weather.find_all("timerange")

    code = []
    # hour_utc = []
    for hour in hours:
        code.append(int(hour.find("value").text))
        if len(code) == 3:
            break 
    return code#,hour_utc


def get_weather(code):
    return WEATHER_CODE[code]
