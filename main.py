from mongodb import myConnection, message
import configparser

config = configparser.ConfigParser()

config.read('config/config.ini')

dbconn = myConnection(config['Databse']['name'], config['Database']['collection'], config['Database']['connstring'])




