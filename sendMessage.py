import requests     # 요청을 하기 위한 모듈
import pprint       #
from decouple import config # decouple 에서부터 config 호출

base_url = 'https://api.telegram.org'
# 안보이게 숨기자
token = config('API_TOKEN') # .env 에서 값을 알아서 찾아 온다.
chat_id = config('CHAT_ID')
# 안보이게 숨기자
text = '😘'

api_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

response = requests.get(api_url)
pprint.pprint(response.json())
