import time
from sys import argv
import time
import numpy as np
import requests
import json
import pickle
import os

from logger import Logger
import utils
from constants import *

# ------------------- EXPERIMENT WITH EDGE INFERENCE -------------------
# ---------------------- MAIN ------------------------

if __name__ == "__main__":

    print("------- RUNNING EXPERIMENT WITH EDGE INFERENCE -------")
    start_time_experiment = time.time()
    filename="experiment_edge_{}.csv".format(start_time_experiment)

    print("------- ------------------ -------")

    log_metrics = Logger(time.time(), "http://{}:{}".format(IP_PROMETHEUS_SERVER, PORT_PROMETHEUS_SERVER), metrics)
    log_metrics.start()

    # START EDGE SAMPLING ON THE XAVIER

    # SETTING SERVER INFERENCE ROUTE TO EDGE
    inference_server_url = "http://{}:{}/{}".format(IP_XAVIER,PORT_FURCIFER_NGINX, SERVER_FULL_MODEL_ROUTE)
    utils.set_inference_server_url(IP_XAVIER,SERVER_FULL_MODEL_ROUTE)

    time.sleep(5)
    
    for i in range(NUMBER_SPOTS):

        start_time=time.time()

        # START SAMPLING ON THE XAVIER

        print("Starting sampling on the xavier")
        utils.start_sampling(IP_NANO, 1)

        while time.time() - start_time > TIME_PER_SPOT_IN_SECONDS:
            
            # WRITE LOGS LOCALLY
            file=open(os.path.join(LOGS_PATH,filename), "a").write(log_metrics.get_metrics() + "\n")
            
        utils.stop_sampling(IP_NANO,1)
        file.close()

        print("Stopped sampling")
        print("Please move to the next location")
        
        time.sleep(3)
















