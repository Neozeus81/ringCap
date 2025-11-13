#!/bin/python3

import pymongo
import json
import datetime



class myConnection:
    def __init__(self, dbName, collectionName, url):
        self.client = pymongo.MongoClient(url)
        self.db = self.client[dbName]
        self.col = self.db[collectionName]

    def insert(self, msg):
        self.col.insert_one(msg)



class message:
    def __init__(self, pcap, event_type):
        self.pcap = pcap
        self.event_type = event_type

    def buildMsg(self):
        message = {
            "pcap" = self.pcap
            "event_type" : self.even
            "timestamp" : datetime.datetime.now().timestamp()
        }
        print(json.dumps(message))
        return message


