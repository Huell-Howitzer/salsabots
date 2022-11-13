import os
import requests

from dotenv import load_dotenv


url = "https://coingecko.p.rapidapi.com/simple/supported_vs_currencies"

key = os.getenv('X_RAPIDAPI_KEY')
host = os.getenv('X_RAPIDAPI_HOST')
headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": host,
}

response = requests.request("GET", url, headers=headers)

print(response.text)