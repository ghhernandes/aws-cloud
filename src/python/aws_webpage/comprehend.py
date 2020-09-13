from aws_webpage import app 
from flask import render_template, request
import json
import requests as r

API_URL = "API URL here" 

@app.route('/comprehend', methods=['GET', 'POST'])
def comprehend():
    if request.method == 'GET':
        return render_template('comprehend.html') 
    else:
        text = str(request.form['text'])

        response = r.post(API_URL, json={"text": [text]})
        response = json.loads(response.text)['body']
        response = json.dumps(json.loads(response)['ResultList'], indent=4, sort_keys=True)
        print(response)
        return render_template('comprehend.html', 
                text=text,
                response=response)

