from mongodb import myConnection, message
import configparser

config = configparser.ConfigParser()

config.read('config/config.ini')

dbconn = myConnection(config['Database']['name'], config['Database']['collection'], config['Database']['connstring'])

f = open("capture.json", "r")

content = f.read()
print(content)
print(type(content))
myMess = message(content, "live_view")

dbconn.insert(myMess.buildMsg())


