# -*- coding: utf-8 -*-
from kstime import kstime
from flask import render_template, request, redirect, url_for, flash, g, session, jsonify#g는 지역변수가 아니고, 전역변수란다.음??#
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc,func,distinct
from apps import app, db
from sqlalchemy.orm.exc import NoResultFound

from apps.forms import ArticleForm, CommentForm, JoinForm, LoginForm
from apps.models import (
    Article,
    Comment,
    User
)

@app.route('/', methods=['GET'])
def article_list():
    context = {}

    stmt = db.session.query(Comment.article_id, func.count('*').label('comment_count')).group_by(Comment.article_id).subquery()
    context['article_list'] = db.session.query(Article, stmt.c.comment_count).outerjoin(stmt, Article.id==stmt.c.article_id).order_by(desc(Article.date_created)).limit(5)

    # context['article_list'] = Article.query.order_by(desc(Article.date_created)).all()
    context['category_list'] = db.session.query(distinct(Article.category)).all()
    return render_template("home.html", context=context, active_tab='timeline')

@app.route('/<tag>', methods=['GET'])
def article_list_with_tag(tag):
    context = {}

    stmt = db.session.query(Comment.article_id, func.count('*').label('comment_count')).group_by(Comment.article_id).subquery()
    context['article_list'] = db.session.query(Article, stmt.c.comment_count).filter_by(category=tag).outerjoin(stmt, Article.id==stmt.c.article_id).order_by(desc(Article.date_created))
    # context['article_list'] = Article.query.order_by(desc(Article.date_created)).filter_by(category=tag)
    context['category_list'] = db.session.query(distinct(Article.category)).all()

    flash(u'카테고리가 \"' + tag + u'\" 인 게시물입니다.', 'info')

    return render_template("home.html", context=context, active_tab='timeline', tag=tag)


#@before request
#
@app.before_request
def before_request():
    g.user_name = None

    if 'user_id' in session:
        g.user_name = session['user_name']
        g.user_email = session['user_email']
        g.user_id = session['user_id']
#
# @index & article list
#

#
# @Login controllers
#
@app.route('/login', methods=['GET','POST'])
def log_in():
    form = LoginForm()

    if request.method == 'POST':
       if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            try: 
                user = db.session.query(User).filter(User.email==email).one() 
                if not check_password_hash(user.password, password): 
                    flash(u'이메일 혹은 비밀번호가 올바르지 않습니다.', 'danger') 
                    return render_template('user/login.html', form=form, active_tab='log_in') 
                else: 
                    session.permanent = True 
                    session['user_email'] = user.email 
                    session['user_name'] = user.name 
                    session['user_id'] = user.id

                    flash(u'로그인 되었습니다.', 'success')
                    return redirect(url_for('article_list')) 
            except NoResultFound, e: 
                flash(u'이메일 혹은 비밀번호가 올바르지 않습니다.', 'danger') 
                return render_template('user/login.html', form=form, active_tab='log_in') 

    #if GET
    return render_template('user/login.html', form = form, active_tab='log_in')


@app.route('/logout')
def log_out():
    session.clear()
    #if GET
    return redirect(url_for('article_list'))

@app.route('/user/join/', methods=['GET', 'POST'])
def user_join():
    form = JoinForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                email=form.email.data,
                password=generate_password_hash(form.password.data),
                name=form.name.data,
                join_date = kstime(9)
            )

            db.session.add(user)
            db.session.commit()

            flash(u'가입이 완료 되었습니다.', 'success')
            return redirect(url_for('article_list'))
    #if GET
    return render_template('user/join.html', form=form, active_tab='user_join')




#
# @article controllers
#
@app.route('/article/create/', methods=['GET', 'POST'])
def article_create():
    form = ArticleForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 사용자가 입력한 글 데이터로 Article 모델 인스턴스를 생성한다.
            article = Article(
                title=form.title.data,
                author=form.author.data,
                category=form.category.data,
                content=form.content.data,
                date_created = kstime(9)
            )

            # 데이터베이스에 데이터를 저장할 준비를 한다. (게시글)
            db.session.add(article)
            # 데이터베이스에 저장하라는 명령을 한다.
            db.session.commit()

            flash(u'게시글을 작성하였습니다.', 'success')
            return redirect(url_for('article_list'))

    return render_template('article/create.html', form=form, active_tab='article_create')


@app.route('/article/detail/<int:id>', methods=['GET'])
def article_detail(id):
    article = Article.query.get(id)
    comments = Comment.query.order_by(desc(Comment.date_created)).filter_by(article_id=article.id)

    return render_template('article/detail.html', article=article, comments=comments)


@app.route('/article/update/<int:id>', methods=['GET', 'POST'])
def article_update(id):
    article = Article.query.get(id)
    form = ArticleForm(request.form, obj=article)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(article)
            db.session.commit()
        return redirect(url_for('article_detail', id=id))

    return render_template('article/update.html', form=form)


@app.route('/article/delete/<int:id>', methods=['GET', 'POST'])
def article_delete(id):
    if request.method == 'GET':
        return render_template('article/delete.html', article_id=id)
    elif request.method == 'POST':
        article_id = request.form['article_id']
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()

        flash(u'게시글을 삭제하였습니다.', 'success')
        return redirect(url_for('article_list'))


# @app.route('/article/like/<int:id>', methods=['GET'])
# def article_like(id):
#     article = Article.query.get(id)
#     article.like += 1

#     db.session.commit()

#     return redirect(url_for('article_detail', id=id))

@app.route('/article/detail_like',methods=['GET'])
def article_like_ajax():
    id = request.args.get('id',0,type=int)

    article = Article.query.get(id)
    article.like +=1

    db.session.commit()

    return jsonify(id=id)
#base.js에서 특정 버튼을 누를 때 detail_like를 향해서 url을 쏘도록 설정해놨습니다.
#html에서는 눈씻고 찾아도 detail_like를 향한 url_for 구문을 못 찾습니다!!!

#
# @comment controllers
#
@app.route('/comment/create/<int:article_id>', methods=['GET', 'POST'])
def comment_create(article_id):
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comment(
                author=form.author.data,
                email=form.email.data,
                content=form.content.data,
                password=form.password.data,
                date_created = kstime(9),
                article=Article.query.get(article_id)
            )

            db.session.add(comment)
            db.session.commit()

            flash(u'댓글을 작성하였습니다.', 'success')
        return redirect(url_for('article_detail', id=article_id))
    return render_template('comment/create.html', form=form)


@app.route('/comment/delete/<int:id>', methods=['GET', 'POST'])
def comment_delete(id):
    if request.method == 'POST':
        comment = Comment.query.get(request.form['comment_id'])

        if request.form['password'] == comment.password:
            article_id = comment.article_id
            db.session.delete(comment)
            db.session.commit()

            flash(u'댓글을 삭제하였습니다.', 'success')
            return redirect(url_for('article_detail', id=article_id))
        else:
            flash(u'비밀번호가 일치하지 않습니다. 다시 한번 입력해주세요.', 'danger')
            return render_template('comment/delete.html', comment_id=request.form['comment_id'])

    elif request.method == 'GET':
        flash(u'경고! 댓글이 완전히 삭제되니, 다시 한번 확인하시기 바랍니다.', 'warning')
        return render_template('comment/delete.html', comment_id=id)

        
# @app.route('/comment/like/<int:id>', methods=['GET'])
# def comment_like(id):
#     comment = Comment.query.get(id)
#     article_id = comment.article_id
#     comment.like += 1

#     db.session.commit()

#     return redirect(url_for('article_detail', id=article_id))


@app.route('/comment/like_ajax', methods=['GET'])
def comment_like_from_detail():
    id = request.args.get('id', 0, type=int)

    comment = Comment.query.get(id)
    comment.like += 1

    db.session.commit()

    return jsonify(id=id)



#
# @Join controllers
#



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