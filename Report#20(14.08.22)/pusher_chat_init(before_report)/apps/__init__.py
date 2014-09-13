from flask import Flask
import os
import pusher

app = Flask('apps')


p = pusher.Pusher(
  app_id='86694',
  key='f972a4d5dad8da15fa8f',
  secret='79426cf73f672f06c8e6'
)

userlist = {}

import controller