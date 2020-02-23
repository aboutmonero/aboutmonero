
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

