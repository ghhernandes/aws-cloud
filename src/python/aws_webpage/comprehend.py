from aws_webpage import app 
from flask import render_template

@app.route('/comprehend')
def comprehend():
    return render_template('main.html') 
