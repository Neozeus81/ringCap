# ringCap
Framework to collect traffic of IoT devices For research purposes

## shark.py

The script that monitors internet traffic on a given interface, number of packets to collect, and a filename to output too

## mongodb.py

Interface for a mongoDB server to store data collected by shark.py

## data/Model.ipynb

A jupyter notebook used primarily:
    - Pull in the collected data
    - clean it into a feature dataframe
    - Create and train a Sklearn tree model
    - Run performance metrics on trained models

# main.py

    combines shark.py and mongodb.py for ease of use.
    For example:
    `sudo python3 main.py --i wlan0 --d 20 --f output.pcap --e idle`
    will collect 20 packets off of the wlan0 interface, store it in output.pcap while labeling those packets as idle state


