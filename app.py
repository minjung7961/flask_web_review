from flask import Flask, render_template

app = Flask(__name__)

app.debug = True  # 오류를 웹페이지 상에 보여주는 세팅 베포할땐 False


# app.py 파일을 가장 먼저 실행하겠다라는 내용 (그중 이줄부터 실행할 것이란 소리)
if __name__ == '__main__':
    app.run() # 애가 서버 실행시켜줌