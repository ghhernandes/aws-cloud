from . import app

@app.route('/comprehend'):
def comprehend():
    return 'Comprehend'
