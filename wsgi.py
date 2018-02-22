import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    
    with open("/mnt/storage/log.txt", "a") as myfile:
        myfile.write(str(datetime.now())+" : "+socket.gethostname()+"\n")
        
        
    with open("/mnt/storage/log.txt", "r") as myfile:
        data=myfile.read()
        
        
    return "Hello World! Greetings from "+socket.gethostname()+"\n\nLogfile:\n"+data
    


if __name__ == "__main__":
    application.run()
