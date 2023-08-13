from datetime import date

class BColours:
    OK = '\033[37m'
    WARNING = '\033[93m'
    BAD = '\033[91m'

def nullCheck(item):
    if item != None:
        return item
    else:
        return "Unknown"