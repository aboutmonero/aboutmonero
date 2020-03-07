
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, flash, redirect, render_template, request, url_for
import csv
import cache

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


@app.route('/explore.html')
def explore():
    return render_template('explore.html', data = cache.get_latest())

@app.route('/follow.html')
def follow():
    return render_template('follow.html')


@app.route('/learn/<topic>.html')
def topic(topic):
    return render_template('/learn/'+topic+'.html')

