# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, flash, redirect
from apps import app, db
from apps.models import Article

@app.route('/', methods=['GET'])
def article_list():
	context = {}

	context['article_list'] = Article.query.all()

	return render_template("home.html",active_tab='timeline',context=context)

@app.route('/article/create/', methods=['GET','POST'])
def article_create():
	if request.method == "GET":
		return render_template("article/create.html",active_tab='article_create')
	if request.method == "POST":
		article_data = request.form

		article = Article(
			title = article_data['title'],
			author = article_data['author'],
			content = article_data['content'],
			category = article_data['category']
			)

		db.session.add(article)
		db.session.commit()
		
		flash(u'게시글이 작성되었습니다.', 'success')
		
		return redirect(url_for('article_list'))

@app.route('/article/detail/<int:id>', methods=['GET'])
def article_detail(id):
	article = Article.query.get(id)

	return render_template("article/detail.html", article=article)
#
# @error Handlers
#
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500