import socket
from flask import Flask
from datetime import datetime
import os

application = Flask(__name__)
logfile = "/mnt/storage/log.txt"


@application.route("/")
def hello():
    
    with open(logfile, "a") as myfile:
        myfile.write(str(datetime.now())+" : "+socket.gethostname()+"\n")
        
        
    with open(logfile, "r") as myfile:
        data=myfile.read()
        
        
    output = "<html><body><h1>Hello World! Greetings from "+socket.gethostname()+"</h1>\n"
    output += "<h2>Logfile:</h2>\n"
    output += "<pre>"+data+"</pre>\n"
    output += "<a href=\"/clearlog\">Click here to clear the log!</a>\n"
    
    return output   


@application.route("/clearlog")
def clearlog():

    if os.path.isfile(logfile):
        os.remove(logfile)

    
    return redirect(url_for('hello'))


if __name__ == "__main__":
    application.run()
