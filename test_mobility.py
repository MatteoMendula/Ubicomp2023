import time
from sys import argv
import time
import numpy as np
import requests
import json
import pickle

from logger import Logger
import utils
from constants import *

# ------------------- EXPERIMENT 1 -------------------
# ---------------------- MAIN ------------------------

if __name__ == "__main__":

    print("------- RUNNING EXPERIMENT 1 -------")
    start_time_experiment = time.time()
    print("------- ------------------ -------")

    log_metrics = Logger(time.time(), "http://{}:{}".format(IP_PROMETHEUS_SERVER, PORT_PROMETHEUS_SERVER), metrics)
    log_metrics.start()

    # START SAMPLING ON THE NANO
    print("Starting sampling on the nano")
    utils.start_sampling(IP_NANO, 1)
    




















