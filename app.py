from flask import Flask, request
from selenium_final import *
# from selenium_concurrent import *
from multiprocessing import Process
from time import sleep
from threading import Thread

app = Flask(__name__)
use_list = [False, False, False, False]


@app.route('/')
def hello_world():
    return 'Hello sendwish web scrapper!'

@app.route('/webscrap', methods=['POST'])
def webscrap():
    data = request.get_json()
    url_receive = data['url'][0]
    # [todo] 예외처리 필요
    sleep(5)
    
    while True:
        if use_list[0] == False:
            use_list[0] = True
            result1 = Thread(target = first_browser, args=(url_receive,)).start()
            pool.join()
            use_list[0] = False
            return result1
            
        elif use_list[1] == False:
            use_list[1] = True
            result2 = Thread(target = second_browser, args=(url_receive,)).start()
            pool.join()
            use_list[1] = False
            return result2
        
        elif use_list[2] == False:
            use_list[2] = True
            result3 = Thread(target = third_browser, args=(url_receive,)).start()
            pool.join()
            use_list[2] = False
            return result3
        
        elif use_list[3] == False:
            use_list[3] = True
            result4 = Thread(target = fourth_browser, args=(url_receive,)).start()
            pool.join()
            use_list[3] = False
            return result4
            
            
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
