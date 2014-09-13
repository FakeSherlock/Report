# -*- coding: utf-8 -*-
"""
models.py

"""

from apps import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(), default=db.func.now())



# 댓글을 모델에 적용 시키는 방법은 매우 다양할 수 있지만
# 만약 한 클래스 안에 Article과 Comment가 같이 존재한다면 정말 수많은 문제가 발생할 수 있다!
# 생각해보시라 글은 하나인데 댓글이 100개인 경우를...!

# 결론은 외래키를 참조해서 클래스를 다시 만들 겁니다.


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    #외래키입니다. 어느 글에 대한 댓글인지 알기위해 기존 article의 id를 불러오는 겁니다.

    article = db.relationship('Article',
                              backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))
    # backref 부분은 cascade을 주의해서 봐야됩니다.
    # 만약 기존 글이 지워지면 댓글도 같이 지워져야되므로 cascade라는 속성을 통해서 설정해준 것 입니다.

    author = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    content = db.Column(db.Text())
    count = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(), default=db.func.now())
