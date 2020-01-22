from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1 style="color:red; text-align:center;">Hello</h1>'

app.run(host='0.0.0.0', port=8080)