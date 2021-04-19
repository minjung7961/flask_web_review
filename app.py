from flask import Flask, render_template
from data import Articles
app = Flask(__name__)

app.debug = True  # 오류를 웹페이지 상에 보여주는 세팅 베포할땐 False


# 클라이언트가 http://localhost:5000/data 으로 gets 요청들어왔을때 hello world 문구를 리턴해 본다

@app.route('/', methods=['Get'])  # 데코레이터 /data 는 요청 들어왔을 때 저 경로로 중계해 준다는 소리
def index():  # 이름 아무거나 해도 됨
    return render_template("index.html", data="kim") # template 파일 아래를 찾아 클라이언트에게 파일이 아닌 문서로 해석한 다음 보낸다.
    # render_template 첫번째 인자 : 파일, 두번째 인자 : data 값
    # render_template 가 하는 일 html 안에 파이썬 문법 해석해줌 그리고 클라이언트에게 결과 값을 보내줌 이능력을 엔진이라하고 그 엔진명은 진자2라고 함 플라스크 안에 ㄴ장되어있음
@app.route('/articles')
def article():
    articles = Articles()
    return render_template('articles.html', articles=articles)

# app.py 파일을 가장 먼저 실행하겠다라는 내용 (그중 이줄부터 실행할 것이란 소리)
if __name__ == '__main__':
    app.run() # 애가 서버 실행시켜줌