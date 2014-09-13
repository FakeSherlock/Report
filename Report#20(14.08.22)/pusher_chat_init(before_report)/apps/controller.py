# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify
from apps import app, userlist, p
from random import randint


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/chat/<chat_id>')
def chat(chat_id):
    username = userlist[chat_id]['name']
    color = userlist[chat_id]['color']

    return render_template('chat.html', user_id=chat_id, username=username, color=color)

@app.route('/send', methods=['GET'])
def send():
    chat_id = request.args.get('id')
    chat_msg = request.args.get('msg_data')

    chat_name = userlist[chat_id]['name']
    chat_color = userlist[chat_id]['color']
    chat_img_url = userlist[chat_id]['img']

    p['newpusher'].trigger('event_msg', {'name': chat_name, 'msg': chat_msg, 'color': chat_color, 'img': chat_img_url})

    return ""

@app.route('/login', methods=['GET'])
def login():
    chat_name = request.args.get('name_data')
    chat_img_url = request.args.get('img_url')
    chat_color = randint(1,19)

    while(True):
        temp_num = randint(0,1000)
        if str(temp_num) not in userlist:
            break

    chat_id = str(temp_num)
    userlist[chat_id] = {}
    userlist[chat_id]['name'] = chat_name
    userlist[chat_id]['color'] = chat_color
    userlist[chat_id]['img'] = chat_img_url

    return jsonify(chat_id=chat_id)

# @app.route('/logout', methods=['GET'])
# def logout():
#
#
#     return ""