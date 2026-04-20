from __future__ import annotations

import re
from datetime import timedelta

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from db import create_account, fetch_account_by_id, fetch_account_by_username
from portfolio import load_portfolio_profile
from settings import settings

app = Flask(__name__)
app.secret_key = settings.secret_key
app.permanent_session_lifetime = timedelta(minutes=settings.session_lifetime_minutes)


def is_logged_in() -> bool:
    return bool(session.get('loggedin'))


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route('/')
def home():
    if is_logged_in():
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and {'username', 'password'} <= set(request.form):
        username = request.form['username'].strip()
        password = request.form['password']
        account = fetch_account_by_username(username)

        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))

        flash('Incorrect username/password')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and {'fullname', 'username', 'password', 'email'} <= set(request.form):
        fullname = request.form['fullname'].strip()
        username = request.form['username'].strip()
        password = request.form['password']
        email = request.form['email'].strip()

        account = fetch_account_by_username(username)

        if account:
            flash('Account already exists!')
        elif not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.fullmatch(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not fullname or not username or not password or not email:
            flash('Please fill out the form!')
        else:
            create_account(fullname, username, generate_password_hash(password), email)
            flash('You have successfully registered!')
    elif request.method == 'POST':
        flash('Please fill out the form!')

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    if not is_logged_in():
        return redirect(url_for('login'))

    account = fetch_account_by_id(session['id'])
    return render_template('profile.html', account=account)


@app.route('/health')
def health():
    return render_template('health.html')


@app.route('/about')
def about():
    if not is_logged_in():
        return redirect(url_for('login'))

    return render_template('aboutme.html', portfolio=load_portfolio_profile())


if __name__ == '__main__':
    app.run(debug=settings.debug, host=settings.app_host, port=settings.app_port)
