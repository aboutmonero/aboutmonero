
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, flash, redirect, render_template, request, url_for
import csv
import cache
from flask import request 
import time  
app = Flask(__name__)

@app.route('/')
def root():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/']],'../../../usage')
    return render_template('index.html')

@app.route('/index.html')
def index():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/index']],'../../../usage')
    return render_template('index.html')

@app.route('/learn.html')
def learn():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/learn']],'../../../usage')
    return render_template('learn.html')
    

@app.route('/participate.html')
def participate():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/participate']],'../../../usage')
    return render_template('participate.html')

@app.route('/legal.html')
def legal():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/legal']],'../../../usage')
    return render_template('legal.html')


@app.route('/explore.html')
def explore():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/explore']],'../../../usage')
    return render_template('explore.html', data = cache.get_latest())

@app.route('/follow.html')
def follow():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/follow']],'../../../usage')
    return render_template('follow.html')


@app.route('/learn/<topic>.html')
def topic(topic):
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    cache.cache([[time.time(), ip, '/learn/'+topic]],'../../../usage')
    return render_template('/learn/'+topic+'.html')

