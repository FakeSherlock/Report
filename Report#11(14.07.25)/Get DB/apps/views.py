from flask import render_template, Flask, \
request, url_for
#1.import : url_for

from google.appengine.ext import db
#2.import : google appengind
class Photo(db.Model):
	photo = db.BlobProperty()
	memo = db.StringProperty()
#2.bring Photo class
#Blob means Photo or picture in U.S.A

from apps import app

@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html")

@app.route('/upload',methods=['POST'])
def upload_db():
	post_data = request.files['grim']
	text_data = request.files['text_get']
	#post_data is a raw data, not refined data
	#now we will refine the datas
	filestream = post_data.read()
	#make raw data to filestream(picture -> line(string) data)
	upload_data = Photo()
	#bring Photo class, make upload_data -> photo album
	upload_data.photo = db.Blob(filestream)
	upload_data.memo = text_data
	#Blob is a form for google app Engine, So upload_data.photo is a variable for saving refined data
	upload_data.photo.put()
	#.put() is a command for save data in google app engine
	upload_data.memo.put()

	url = url_for("shows", key=upload_data.photo.key())
	#url_for has a grammer like this. "**" part means call ** function and key means 
	memo2 = url_for("memos", key=upload_data.memo.key())
	return render_template("upload.html", url=url, result_memo=memo2)
	

@app.route('/show/<key>')
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data)

@app.route('/memo/<key>')
def memos(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data)

