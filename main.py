from flask import Flask, render_template, request, redirect, url_for, session
import ctypes
from ctypes import *
import sys
import logging
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sus.stdout))
app.logger.setLevel(logging.ERROR)
app.secret_key = 'MY_SUPER_SECRET_KEY'
from databaseuser import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///BarProject.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
DBSession = DBSession()

@app.route('/')
def main():
	return render_template('mainpage.html') 

@app.route('newuser')
def newuser():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		day = request.form['daybirthdate']
		month = request.form['monthbirthdate']
		year = request.form['yearbirthdate']
		birthdate = datetime.date(year, month, day)
		country = request.form['country']
		if username == "" or email == "" or password == "" or firstname == "" or lastname == "" or country == "":
			flash("Your form is missing arguments")
			return redirect(url_for('newuser'))
		if session.query(User).filter_by(email = email).first() is not None:
			flash("A user with this email address already exists")
		if session.query(User).filter_by(username = username).first() is not None:
			flash("A user with this username already exists")
			return redirect(url_for('newuser'))
		User = User(username = username, password = password, email = email, firstname = firstname, lastname = lastname, 
			country = country, birthdate = birthdate)
		customer.hash_password(password)
		session.add(User)
		session.commit()
		flash("User Created Successfully")
		return redirect(url_for('mainpage.html'))
	else:
		return render_template('signup.html')

year = request.form["yearbirthdate"]