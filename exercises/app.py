from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'START HERE: yeahh!!'

# @app.route("/")
# def hello_name_route(name):
#     return render_template(
#         'hello.html', n = name)


@app.route('/hello/<string:name>')
def hello_name_route(name):
    return render_template(
        'hello.html', n = name)

# @app.route("/")
# def home_route(name):
#     return render_template('home_with_link.html')

@app.route("/hello/")
def hello_route(name):
    return render_template('hello_with_link.html')




app.run(debug=True)
