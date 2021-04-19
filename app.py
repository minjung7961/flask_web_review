from flask import Flask, render_template

app = Flask(__name__)

app.debug = True  # 오류를 웹페이지 상에 보여주는 세팅 베포할땐 False


# 클라이언트가 http://localhost:5000/data 으로 gets 요청들어왔을때 hello world 문구를 리턴해 본다

@app.route('/data', methods=['Get'])  # 데코레이터 /data 는 요청 들어왔을 때 저 경로로 중계해 준다는 소리
def index():  # 이름 아무거나 해도 됨
    return "hello world"


# app.py 파일을 가장 먼저 실행하겠다라는 내용 (그중 이줄부터 실행할 것이란 소리)
if __name__ == '__main__':
    app.run() # 애가 서버 실행시켜줌