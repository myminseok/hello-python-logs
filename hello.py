import os
from flask import Flask
from time import sleep
import threading

app = Flask(__name__)

@app.route('/')
def hello():
	print('Hello World BLUE!')
	return 'Hello World BLUE!'

# https://tiagohorta1995.medium.com/python-flask-api-background-task-96bf1120a855
thread_event = threading.Event()
def backgroundTask():
    while thread_event.is_set():
        print('Background task running!')
        #sleep(5)
        
#@app.route("/start", methods=["POST"])
@app.route("/start")
def startBackgroundTask():
    try:
        thread_event.set()
        
        thread = threading.Thread(target=backgroundTask)
        thread.start()

        return "Background task started!"
    except Exception as error:
        return str(error)
    
#@app.route("/stop", methods=["POST"])
@app.route("/stop")
def stopBackgroundTask():
    try:
        thread_event.clear()

        return "Background task stopped!"
    except Exception as error:
        return str(error)


port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
