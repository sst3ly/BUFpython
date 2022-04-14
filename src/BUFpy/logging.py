import time
from datetime import datetime

class Logger():
    def __init__(self, file=None, logTime=True):
        if(file != None):
            self.file = file
        if(type(logTime) == bool):
            self.logTime = logTime
            
    def settings(self, file=None, logTime=None):
        if(file == None):
            file = self.file
        if(logTime == None):
            logTime = self.logTime
        
        if(file != self.file and type(file) == str):
            self.file = file
        if(logTime != self.logTime and type(logTime) == bool):
            self.logTime = logTime
        
    def log(self, level, message):
        #date+time
        
        dt = datetime.now()
        
        #to log
        if(self.file == None):
            raise Exception("No file selected for logging")
        
        clsfy = level
        if(level == -1):
            clsfy = "ERROR"
        if(level == 0):
            clsfy = "INFO"
        if(level == 1):
            clsfy = "WARNING"
        #logging
        if(level != "" and level != None):
            with open(self.file, 'a') as f:
                data = f"[{dt}][{clsfy}] : {message}"
                f.write(data)
        else:
            with open(file, 'a') as f:
                data = f"[{dt}] {message}"
                f.write(data)
                
    def logCustom(self, toLog):
        with open(self.file, 'a') as f:
                f.write(toLog)