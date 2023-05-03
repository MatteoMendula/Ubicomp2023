import time
from sys import argv
import time
import numpy as np
import requests
import json
import pickle

from logger import Logger
import utils


# ------------------- EXPERIMENT 1 -------------------
# ------------------- SETTINGS -----------------------
path='./github_experiments/Ubicomp2023'

metrics = []
metrics.append("energon_cpu_in_power_mW")
metrics.append("energon_gpu_in_power_mW")
metrics.append("energon_cpu_total_usage_percentage")
metrics.append("energon_gpu_total_usage_percentage")
metrics.append("energon_ram_used_percentage")
metrics.append("furcifer_latency_ms")
metrics.append("furcifer_fps")

IP_XAVIER = "10.42.0.84"
IP_NANO = "10.42.0.120"
IP_PROMETHEUS_SERVER = "localhost"

PORT_FURCIFER_COMMAND_SERVER = "7999"
PORT_ENERGON_EXPORTER = "9877"
PORT_FURCIFER_EXPORTER = "9878"
PORT_PROMETHEUS_SERVER = "9090"

ROUTE_TO_START_SAMPLING = "sample_camera_and_send_image_for_inference"
ROUTE_TO_STOP_SAMPLING = "stop_sampling"
ROUTE_TO_SET_INFERENCE_SERVER_URL = "set_server_url"
ROUTE_TO_EXCUTE_COMMAND = "execute_command"

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
    




















