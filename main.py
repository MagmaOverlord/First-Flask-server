import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
  return flask.send_file('static/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)