from flask import Flask, render_template, url_for
from instagram.client import InstagramAPI
import os

app = Flask(__name__)
api = InstagramAPI(client_id='63b8fc9a82454cdfbf6e9899d4b7547e')

#TODO: 
#get tags working...
#analytics
#google ads
#background worker with redis? mongo?

@app.route('/')
def home():
    tags = map(lambda x: x.name, api.tag_search("insta", 30)[0])
    return render_template('index.html', tags=tags)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

