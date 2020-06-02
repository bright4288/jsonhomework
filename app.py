from flask import Flask, request, render_template, redirect, url_for, session,abort

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = request.form['username']
			return render_template('index.html', data=username)
		return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return '로그인 안됨'
		except:
			return "로그인 다시하시오"

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        name = request.form["username"]
        passw = request.form["password"]
        return 'POST 이다. 학번은: {} 이름은: {}'.format(name, passw)


@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = b'aaa!111/'
    app.run(debug=True)