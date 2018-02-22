import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    
    with open("/mnt/storage/log.txt", "a") as myfile:
        myfile.write(str(datetime.now())+" : Pod: "+socket.gethostname())
        
    return "Hello World! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
