from flask import Flask
import pusher
import os

app = Flask('apps')
p = pusher.Pusher(
    app_id='85794',
    key='1802788264cce3e72178',
    secret='0b2e5345c80cc387316d'
)

userlist = {}

import controller