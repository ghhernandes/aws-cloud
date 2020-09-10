from aws_webpage import app 
from flask import render_template, request

import requests as r

API_URL = "yep your api url" 

@app.route('/comprehend', methods=['GET', 'POST'])
def comprehend():
    if request.method == 'GET':
        return render_template('comprehend.html') 
    else:
        text = str(request.form['text'])

        api_request = r.post(API_URL, data={"text": [text]})
        return render_template('comprehend.html', text=api_request.content.decode('utf8'))

