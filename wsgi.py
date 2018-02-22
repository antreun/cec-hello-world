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
        
        
    output = "<html><body><h1>Hello World! Greetings from "+socket.gethostname()+"</h1>\n"
    output += "<h2>Logfile:</h2>\n"
    output += "<pre>"+data+"</pre></body></html>"
    
    return output   


if __name__ == "__main__":
    application.run()
