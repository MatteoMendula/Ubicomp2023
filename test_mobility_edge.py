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
    filename="experiment_edge_{}.pkl".format(start_time_experiment)

    print("------- ------------------ -------")

    log_metrics = Logger(time.time(), "http://{}:{}/api/v1/query?query=".format(IP_PROMETHEUS_SERVER, PORT_PROMETHEUS_SERVER), metrics)
    log_metrics.start()

    
    # SETTING SERVER INFERENCE ROUTE TO LOCAL
    inference_server_url = "http://localhost:8001/{}".format(SERVER_FULL_MODEL_ROUTE)
    utils.set_inference_server_url(IP_NANO,inference_server_url)

    time.sleep(5)
    
    for i in range(NUMBER_SPOTS):

        start_time=time.time()

        # START SAMPLING ON THE XAVIER

        print("Starting sampling on the xavier")
        utils.start_sampling(IP_NANO, 1)

        while time.time() - start_time <= TIME_PER_SPOT_IN_SECONDS:
            
            # WRITE LOGS LOCALLY
            with open(os.path.join(LOGS_PATH,filename), 'wb') as f:
                pickle.dump(log_metrics.get_metrics(),f)

        utils.stop_sampling(IP_NANO,1)
        f.close()

        print("Stopped sampling")
        print("Please move to the next location")
        
        time.sleep(3)
















