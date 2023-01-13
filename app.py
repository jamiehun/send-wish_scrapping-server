from flask import Flask, request
from selenium_main import web_scrap
import threading
from selenium_main import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello sendwish web scrapper!'

# @app.before_request
# def before_request():

@app.route('/webscrap', methods=['POST'])
def webscrap():
    data = request.get_json()
    url_receive = data['url'][0]
    # [todo] 예외처리 필요
    
    t = threading.Thread(target = web_scrap, args=(url_receive))
    t.start()
    result = t.join()
    # result = web_scrap(url_receive)
    
    return result

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
