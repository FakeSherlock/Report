# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
	render_template
from apps import app
from database import Database

dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)
										#'entries=entires' part means reloading data from database

@app.route('/add', methods=['POST'])
def add_entry():
	storage={}
	#for saving data, we use type of dictionary
	storage['num'] = dataStorage.num
	storage['count'] = 0
	storage['title'] = request.form['title']
	storage['contents'] = request.form['contents']
	#This Database has 4 attribute for the serviece
	dataStorage.put(storage)
	#from database.py, we use function put()
	
	
	dataStorage.num+=1

	return redirect(url_for('show_entries'))

@app.route('/del/<idx>', methods=['GET'])
# < idx > means some value that comes from somewhere it's not fixed
def del_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			#Method "GET" always return "string" type value.
			dataStorage.database.remove(data)
			break
			#break exist for efficient way for searching and reducing time
	return redirect(url_for('show_entries'))

@app.route('/plus/<idx>', methods=['GET'])
def plus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['count']+=1
			break
	dataStorage.database = sorted(dataStorage.database, key=lambda list:list['count'], reverse=True)
	#sorted function grammer looks like this, 
	# key means who's gonna get sorted 
	# and list means condition of sorting (+ 'list'=datastorage.database)
	# reverse=true means first one is greater one, last is minimum value
	return redirect(url_for('show_entries'))

@app.route('/not_plus/<idx>', methods=['GET'])
def not_plus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['count']-=1
			break
	dataStorage.database = sorted(dataStorage.database, key=lambda list:list['count'], reverse=True)
	return redirect(url_for('show_entries'))

@app.route('/modify/<idx>', methods=['GET'])
def modify_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['title']=request.args['title']
			data['contents']=request.args['contents']
			#Methods 'GET' -> request.args
			#Methods 'POST' -> request.form
			break
	return redirect(url_for('show_entries'))

@app.route('/ascending_sort', methods=['GET'])
def ascending_sort_entry():
	dataStorage.database = sorted(dataStorage.database, key=lambda list:list['count'], reverse=True)
	return redirect(url_for('show_entries'))

@app.route('/descending_sort', methods=['GET'])
def descending_sort_entry():
	dataStorage.database = sorted(dataStorage.database, key=lambda list:list['count'], reverse=False)
	return redirect(url_for('show_entries'))