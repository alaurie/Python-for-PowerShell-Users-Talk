#! /usr/bin/env python
import argparse
import requests

arg_parser = argparse.ArgumentParser(
    prog="get-weather", description="Get weather for entered city."
)

arg_parser.add_argument(
    "city", metavar="my_city", type=str, help="City for which you want to get weather."
)


def get_city_weather(search_city):
    api_key = "2fe992c00735713d86f2d6577ff41a3d"
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q="
    response = requests.get(url + search_city)
    return response.json()


if __name__ == "__main__":
    args = arg_parser.parse_args()
    try:
        weather = get_city_weather(args.city)
        print(f"The weather in {args.city}: {weather['weather'][0]['description']}")
    except KeyError:
        print("City no found.")
