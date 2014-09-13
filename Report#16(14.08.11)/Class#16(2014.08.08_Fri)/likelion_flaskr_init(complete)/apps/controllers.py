# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, flash, redirect
from apps import app, db
from sqlalchemy import desc
from apps.models import Article, Comment

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
    comments = article.comments.order_by(desc(Comment.date_created)).all()
    # 값에 따른 정렬 방법입니다. 유의해서 보시길!
    return render_template("article/detail.html", article=article, comments=comments)

@app.route('/article/update/<int:id>', methods=['GET', 'POST'])
def article_update(id):
    article = Article.query.get(id)
    if request.method == 'GET':
        check = True
        title = article.title
        author = article.author
        category = article.category
        content = article.content
        return render_template('article/update.html',check=check, title=title, author=author, category=category, content=content)
    
    elif request.method == 'POST':
        check = False
        article_data = request.form
        #새 데이터를 담을 프레임을 생성합니다.
        
        article = Article.query.get(id)
        #기존 데이터를 id를 식별인자로 해서 불러온 후 article 변수에 저장합니다.
        #update 가장 첫 줄과 중복되는데 사실 54번 째 줄을 지워도 됩니다.

        article.title = article_data['title']
        article.author = article_data['author']
        article.category = article_data['category']
        article.content = article_data['content']
        #기존 데이터를 덮어씌워줍니다(update) 

        db.session.commit()
        #데이터베이스에 올립니다.

        flash(u'게시글이 수정되었습니다.', 'success')
        return redirect(url_for('article_detail', id=id, check=check))

@app.route('/article/delete/<int:id>', methods=['GET', 'POST'])
def article_delete(id):
    if request.method == 'GET':
        return render_template('article/confirm.html', article_id=id)

    elif request.method == 'POST':
        article = Article.query.get(id)

        db.session.delete(article)
        db.session.commit()
        flash(u'게시글을 삭제하였습니다.', 'success')

        return redirect(url_for('article_list'))

#
# @comment controllers
#
@app.route('/comment/create/<int:article_id>', methods=['GET', 'POST'])
def comment_create(article_id):
    if request.method =='GET':
        return render_template('comment/create.html')
    
    elif request.method == 'POST':

        comment_data = request.form

        comment = Comment(
            
            author = comment_data['author'],
            email = comment_data['email'],
            content = comment_data['content'],
            password = comment_data['password'],
            article = Article.query.get(article_id)
        )

        db.session.add(comment)
        db.session.commit()

        flash(u'댓글을 작성하였습니다.', 'success')
        return redirect(url_for('article_detail', id=article_id))

@app.route('/comment/delete/<int:comment_id>', methods=['GET', 'POST'])
def comment_delete(comment_id):
    comment=Comment.query.get(comment_id)

    if request.method == 'GET':
        return render_template('comment/before_confirm.html', comment_id=comment_id)

    elif request.method =='POST':
        if comment.password == request.form['password']:
            db.session.delete(comment)
            db.session.commit()
            flash(u'댓글을 삭제하였습니다.', 'success')
            
            return redirect(url_for('article_detail', id=article_id))

        else:
            flash(u'비밀번호가 일치하지 않습니다.', 'success')
            return render_template('comment/before_confirm.html', comment_id=comment_id)

# @app.route('/article/delete/<int:id>', methods=['GET', 'POST'])
# def article_delete(id):
#     if request.method == 'GET':
#         return render_template('article/confirm.html', article_id=id)

#     elif request.method == 'POST':
#         article = Article.query.get(id)

#         db.session.delete(article)
#         db.session.commit()
#         flash(u'게시글을 삭제하였습니다.', 'success')

#         return redirect(url_for('article_list'))

@app.route('/comment/plus/<int:comment_id>', methods=['GET', 'POST'])
def comment_plus(comment_id):
    comment = Comment.query.get(comment_id)
    comment.count += 1

    article_id=comment.article_id
    
    db.session.merge(comment)
    db.session.commit()

    return redirect(url_for('article_detail', id=article_id))

@app.route('/comment/update/<int:comment_id>', methods=['GET', 'POST'])
def comment_update(comment_id):
    comment = Comment.query.get(comment_id)
    article_id = comment.article_id

    if request.method == 'GET':
        check = True
        # comment = comment.content
        # author = comment.author
        # password = comment.password
        # email = comment.email
        return render_template('comment/update.html',check=check, \
            content=comment.content, author=comment.author, password=comment.password, email=comment.email)

    
    elif request.method == 'POST':
        check = False
        comment_data = request.form
        #새 데이터를 담을 프레임을 생성합니다.

        comment.content = comment_data['content']
        comment.author = comment_data['author']
        comment.password = comment_data['password']
        comment.email   = comment_data['email']
        #기존 데이터를 덮어씌워줍니다(update) 

        db.session.commit()
        #데이터베이스에 올립니다.

        flash(u'댓글이 수정되었습니다.', 'success')
        return redirect(url_for('article_detail', id=article_id))

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