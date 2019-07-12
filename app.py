from flask import Flask, request
from decouple import config # decouple 에서부터 config 호출
import pprint
import requests # 요청

app = Flask(__name__)

# Telegram info
API_TOKEN = config('API_TOKEN') # 상수는 대문자
# Naver info
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')

base_url = 'https://api.telegram.org'

@app.route('/')
def hello():

    return 'Hello World'


@app.route('/greeting/<name>')
def greeting(name):
    return f'Hello, {name}'


@app.route(f'/{API_TOKEN}', methods=['POST'])   # POST 요청으로만 받겠다.
def telegram():
    from_telegram = request.get_json()
    # pprint.pprint(from_telegram)
    if from_telegram.get('message') is not None:    # 딕셔너리에 대괄호 접근; 내용이 없으면 error
        # 우리가 원하는 로직을 쌓아간다.              # get으로 접근; 내용이 없어도 작동 None
        chat_id = from_telegram.get('message').get('chat').get('id')    # 보낸 사람의 아이디
        text = from_telegram.get('message').get('text')                 # 보낸 메세지

        # 첫 네글자가 '/번역 ' 일 때
        if text[0:4] == '/한영 ':   # 텍스트도 index 로 접근이 가능하다.
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,   # , 있는걸 추천 컨벤션 추가할때 혹시라도 오류가 생길까봐
            }                                                   # trailing comma
            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:],   # '/번역 ' 이후의 문자열만 대상으로 번역
            }
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            papago_res = requests.post(papago_url, headers=headers, data=data)
            # pprint.pprint(papago_res.json())
            text = papago_res.json().get('message').get('result').get('translatedText')
        if text[0:4] == '/영한 ':   # 텍스트도 index 로 접근이 가능하다.
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
            }
            data = {
                'source': 'en',
                'target': 'ko',
                'text': text[4:],   # '/번역 ' 이후의 문자열만 대상으로 번역
            }
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            papago_res = requests.post(papago_url, headers=headers, data=data)
            # pprint.pprint(papago_res.json())
            text = papago_res.json().get('message').get('result').get('translatedText')

        api_url = f'{base_url}/bot{API_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(api_url)


    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
