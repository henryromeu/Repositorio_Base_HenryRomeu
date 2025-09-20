from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/planos')

def planos():
    return render_template('planos.html')