from flask import Flask, request, render_template
app = Flask(__name__)

import game
import json

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/hello')
def hellohtml():
    return render_template("hello.html")

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return "{0}님 반갑습니다. (HP {1})으로 게임을 시작 합니다.".format(character["name"],character["hp"])


@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        # args_dict = request.args.to_dict()
        # print(args_dict)
        num = request.args["num"]
        name = request.args.get("name")

        return "GET으로 전달된 데이터({}, {})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        with open("static/save.txt","w", encoding='utf-8') as f:
            f.write("%s,%s" % (num, name))
        return "POST로 전달된 데이터({}, {})".format(num, name)

@app.route('/getinfo')
def getinfo():
    # 파일 입력
    with open("static/save.txt", "r", encoding='utf-8') as file:
        student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])

if __name__ == '__main__': 
    app.run(debug=True)



