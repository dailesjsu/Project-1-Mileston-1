from flask import Flask
from flask import render_template
#from form import LoginForm
#LoginForm class inside the form.py

app = Flask(__name__)


@app.route('/')
def finance():
    name = 'buddy'
    title = 'Cash Course'

    return render_template('login.html', homen=name, title=title)


@app.route('/afterlogin')
def afterlogin():
    name = 'buddy'
    title = ''

    return render_template('afterlogin.html', homen=name, title='Cash Course')


@app.route('/expenditure')
def spending():
    name = 'buddy'
    title = ''

    return render_template('spending.html', homen=name, title='Expenditure')


@app.route('/income')
def income():
    name = 'buddy'
    title = ''

    return render_template('income.html', homen=name, title='Income')
@app.route('/register')
def register():
    name= 'buddy'
    title=''
    return render_template('register form.html', homen=name, title='Income')
def register2():
    name= 'buddy'
    title=''
    return render_template('register sucessful.html', homen=name, title='Income')


if __name__ == '__main__':
    app.run()