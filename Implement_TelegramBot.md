# TelegramBot 만들기

## Bot 만들기

### BotFather

`/new bot` 으로 새로운 봇 생성

http API token 을 받아 외부에 노출되지 않도록 관리한다.

### Making Requests

http://api.telegram.org/bot<token>/METHOD_NAME

API에 요청을 보낼 수 있는 주소

token값과 API에서 제공하는 METHOD로 이루어져있다.

/getMe 를 통해 chat_id 를 알 수 있다.

### sendMessage

Required == Yes 인 항목은 반드시 포함되어야 한다.`chat_id`와 `text`

/sendMessage?chat_id={chat_id}&text={text}

method 뒤에 ?를 쓰고 각각의 항목을 &로 구분한다.

### decouple

```bash
$ pip install decouple
```

decouple 모듈을 설치한다

```python
from decouple import config # decouple 에서부터 config 호출
# 안보이게 숨기자
token = config('API_TOKEN') # .env 에서 값을 알아서 찾아 온다.
chat_id = config('CHAT_ID')
```

.env 환경변수 파일을 이용해 외부로부터 변수들을 숨길 수 있도록 해준다.

config 함수를 이용해 .env 파일 안에 숨겨놓은 값들을 가져온다.

### setWebhook

#### ngrok

```bash
$ ./ngrok.exe http 5000
```

ngrok을 이용해 로컬 서버에 접속할 수 있게 해준다.

#### Python Anyware

서버를 제공받아 내가 만든 코드를 배포한다.

/setWebhook?url={ngrok제공 주소 or PythonAnyware제공 주소}/{API_TOKEN}



### Etc.

#### GET 요청

주소창에 엔터를 치고 들어가는 것은 get 요청이다.

#### POST 요청

아이디, 비밀번호 같은 중요한 요청을 보낼 때

/register?id=Myreal_id&pwd=Myreal_pwd 와 같은 방식으로 보낸다면 해킹의 위험이 생긴다.

따라서 게시글 작성 및 삭제 요청, 회원가입 요청 등

아주 중요한 요청을 보낼 때, POST 요청을 사용해 정보를 숨겨서 보낼 수 있다.

