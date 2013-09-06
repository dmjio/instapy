from flask import Flask, render_template, url_for
from instagram.client import InstagramAPI
import os

app = Flask(__name__)
api = InstagramAPI(client_id='63b8fc9a82454cdfbf6e9899d4b7547e')

#get tags working...

@app.route('/')
def home():
    tags = api.media_popular(count=20)
    return render_template('index.html', tags=tags)
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
