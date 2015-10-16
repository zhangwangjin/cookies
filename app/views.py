# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from app import app
from flask import render_template, session, request, redirect, url_for
from forms import RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('User_Base.html', )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    else:
        return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST'and form.validate():
        return redirect(url_for('index'))
    elif form.csrf_token.errors:
        pass
    return render_template('register.html', form=form)