from flask import Flask, request
from decouple import config # decouple 에서부터 config 호출
import pprint
import requests # 요청

app = Flask(__name__)
API_TOKEN = config('API_TOKEN') # 상수는 대문자
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

        if text == '안녕':
            text = '오셨습니까'

        api_url = f'{base_url}/bot{API_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(api_url)


    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
