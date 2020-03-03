
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, flash, redirect, render_template, request, url_for
import csv

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/learn.html')
def learn():
    return render_template('learn.html')
    

@app.route('/participate.html')
def participate():
    return render_template('participate.html')


@app.route('/statistics.html')
def statistics():
    return render_template('statistics.html')

@app.route('/newsletter.html')
def newsletter():
    return render_template('newsletter.html')


@app.route('/learn/<topic>.html')
def topic(topic):
    return render_template('/learn/'+topic+'.html')

