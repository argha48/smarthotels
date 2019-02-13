#!/usr/bin/env python
from flaskexample import app
# from dotenv import load_env
app.secret_key = 'super secret key'
app.run(host='0.0.0.0', debug = True)
