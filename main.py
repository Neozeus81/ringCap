from mongodb import myConnection, message
from shark import Shark
import configparser
import argparse

config = configparser.ConfigParser()
parser = argparse.ArgumentParser(description="Automated sniff script to send .pcap files as json to a mongoDB interface")
parser.add_argument("--i", help="Interface the Access point the ring is connected to")
parser.add_argument("--d", help="Duration in seconds")
parser.add_argument("--f", help="output file name")
parser.add_argument("--e", help="Event type [ idle, motion, live_feed]")

args = parser.parse_args()

config.read('config/config.ini')

dbconn = myConnection(config['Database']['name'], config['Database']['collection'], config['Database']['connstring'])

myshark = Shark(args.d, args.i, args.f)

myshark.sniff()

f = open(args.f, "r")

content = f.read()

myMess = message(content, args.e)

dbconn.insert(myMess.buildMsg())


