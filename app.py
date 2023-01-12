from flask import Flask, request
from selenium_main import web_scrap
from pathos.multiprocessing import ProcessPool as Pool
from time import sleep
import time 
import threading

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello sendwish web scrapper!'

@app.route('/webscrap', methods=['POST'])
def webscrap():
    data = request.get_json()
    url_receive = data['url'][0]
    sleep(1)
    # [todo] 예외처리 필요
    
    lock = threading.Lock()
    
    lock.acquire()
    result = web_scrap(url_receive)
    lock.release()
    
    return result    
    
    # pool = Pool(processes = 3)
    # for result in pool.map(web_scrap, url_receive):
    #     sleep(1)
    #     return result
    
    return pool.map(web_scrap, url_receive)
        
    # return web_scrap(url_receive)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
