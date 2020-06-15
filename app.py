from flask import Flask, request, render_template, redirect, url_for, session, abort

import dbdb
import game
import json

app = Flask(__name__)
app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

#순서 1
@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html',data=character)

#순서 2
@app.route('/gamestart')
def gamestart():
    with open("static/game.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['house'])
    return "{} 이 {} 을 골랐습니다.".format(character["name"],character["house"][0])

#순서 3
@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/game.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['house'])
        return "로딩중 , 이상한 세계 1에 오신 것을 환영합니다. {}이 {}을 지었습니다. 둘 중 선택하시오 1번 2번".format(character["name"],character["house"][0])
    elif num == 2:
        return "로딩 실패, 처음으로 돌아가세요"
    elif num ==3:
        return "퉁퉁이"
    else:
        return "없어요"
    #return 'Hello, {}!'.format(name)

#순서 4
@app.route('/home/<int:num>')
def home(num):
    if num == 1:
        return "깨져 버림"
    elif num == 2: 
        return "안 깨짐 도구를 사용하시오. 1. 노동 2. 노동X"
    else:
        return "처음으로 돌아가시오"

#순서 5
@app.route('/노동/<int:num>')
def work(num):
    if num == 1:
        with open("static/game.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['tools'])
        return "노동도구인 {}을 선택하였습니다.".format(character["tools"][0])
    elif num ==2:
        with open("static/game.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['tools'])
        return "노동 도구가 아닌 {}을 선택하였습니다.".format(character["tools"][2])
    else:
        return "처음으로 돌아가시오"
#순서 6
@app.route('/flower/<name>')
def flower(name):
    character = game.set_charact(name)
    return render_template('flower.html',data=character)
#순서 7
@app.route('/flower/<int:num>')
def input_flower(num):
    if num == 1:
        with open("static/game.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['kind'])
        return "{}이 자랐습니다. 게임 성공".format(character["kind"][2])
    elif num ==2:
        with open("static/game.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['kind'])
        return "{}이 자랐습니다. 게임 실패".format(character["kind"][1])
    else:
        return "아무것도 안심음"
        
#로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print(id,type(id))
        print(pw,type(pw))
        #id와 pw가 db 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        ret = dbdb.select_user(id,pw)
        print(ret)
        if ret != None:
            session['user'] =id
            return redirect(url_for('index'))
            # return "안녕하세요 ~ {} 님".format(ret[2])
        else:
            return redirect(url_for('login'))
            # return "아이디 또는 패스워드를 확인 하세요.".format()

@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('index'))

#회원가입
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        print(id,type(id))
        print(pw,type(pw))
        ret= dbdb.check_id(id)
        if ret != None:
            return '''
                    <script>
                    alert('다른 아이디를 사용하세요');
                    location.href='/join';
                    </script>
                    '''
        #id와 pw가 db 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        dbdb.insert_user(id,pw,name)
        return redirect(url_for('login'))


@app.route('/form')
def form():
	return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
	if request.method == 'GET':
		return 'GET 으로 전송이다.'
	else:
		num = request.form['num']
		name = request.form['name']
		print(num, name)
		dbdb.insert_data(num, name)
		return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/getinfo')
def getinfo():
    if 'user' in session:
        ret = dbdb.select_all()
        print(ret[3])
        return render_template('getinfo.html', data=ret)

    return redirect(url_for('login'))
# 	# return '번호 : {} 이름: {}'.format(ret[0], ret[1])

if __name__ == '__main__':
    app.run(debug=True)
