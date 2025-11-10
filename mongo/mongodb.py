from pymongo import MongoClient
import configparser

config = configparser.ConfigParser()

config.read('../config/config.ini')

print(config['Database']['connstring'])
client = MongoClient(config['Database']['connstring'], tlsAllowInvalidCertificates=True, tlsCertificateKeyFile=config['Database']['pem'])
db = client[config['Database']['name']]
col = db[config['Database']['collection']]

temp = {"name":"Hello world", "temp":"ok"}

x = col.insert_one(temp)


