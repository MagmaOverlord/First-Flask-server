import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
  return flask.send_file('static/index.html') 


@app.route('/about')
def about():
  return flask.send_file('static/about.html')

@app.route('/iceCream/<num>')
def iceCreamNumber(num):
    output = "You chose "+num+" Mint Chocolate Chip Ice Creams, which is more than " +str(int(num)-1)
    output += "<br/><a href = '/'>Home</a>";
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)