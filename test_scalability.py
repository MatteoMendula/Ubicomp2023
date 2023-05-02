import time
from sys import argv
import time
import numpy as np
import argparse

from user import User
from logger import Logger
from inference_metrics_exporter import InferenceMetricsExporter

import pickle

# experiment settings
parser = argparse.ArgumentParser()

parser.add_argument(
    "-u",
    "--url",
    nargs="?",
    default="http://localhost:8000/furcifer_efficientnet_b0",
    type=str,
    help="URL of the server",
)
parser.add_argument(
    "-d",
    "--duration",
    nargs="?",
    default=10,
    type=int,
    help="Duration of the experiment",
)
parser.add_argument(
    "-t",
    "--n_tests",
    nargs="?",
    default=10,
    type=int,
    help="Number of tests",
)
parser.add_argument(
    "-p",
    "--prometheus_server_url",
    nargs="?",
    default="http://localhost:9090/api/v1/query?query=",
    type=str,
    help="Prometheus server url",
)
args = parser.parse_args()

metrics = []
metrics.append("energon_cpu_in_power_mW")
metrics.append("energon_gpu_in_power_mW")
metrics.append("energon_cpu_total_usage_percentage")
metrics.append("energon_gpu_total_usage_percentage")
metrics.append("energon_ram_used_percentage")
metrics.append("furcifer_latency_ms")

if __name__ == "__main__":

    print("------- RUNNING EXPERIMENT -------")

    start_time_user = time.time()

    url = args.url
    duration_user = args.duration
    num_tests = args.n_tests
    prometheus_server_url = args.prometheus_server_url
    print("running with service server on: ", url)
    print("------- ------------------ -------")



    inference_metric_exporter = InferenceMetricsExporter()
    # inference_metric_exporter.setDaemon(True)
    inference_metric_exporter.start()

    # wait for the InferenceMetricsExporter server to start
    print("Waiting for the InferenceMetricsExporter to start...")
    for i in range(5):
        print(5-i)
        time.sleep(1)

    duration_metrics = (duration_user * num_tests) + 3
    log_metrics = Logger(time.time(), duration_metrics, prometheus_server_url, metrics)
    # log_metrics.setDaemon(True)
    log_metrics.start()

    #avg_var_metrics={}
    tot_requests = 100
    n_requests=1
    cum_metrics=[]

    #path
    path='/home/sharon/Documents/Research/Ubicomp_Experiments/github_experiments/Ubicomp2023'
    while n_requests < tot_requests:
        for j in range(num_tests):
            if j == 0 :
                num_tests=20
            else:
                num_tests=10

            print("Testing "+ str(n_requests) + " requests per second")
            start_time_user=time.time()
            user_1=User(type_conenction='BAD', set_tasks=set(), req_per_sec=n_requests, url=url, start_time=start_time_user, duration=duration_user, inference_metric_exporter=inference_metric_exporter)
            user_1.start()
        
            print("Getting the metrics ")
            results_metrics=log_metrics.get_metrics(start_time_user,start_time_user+duration_user)
            cum_metrics.append(results_metrics)
            print(results_metrics)
            del user_1

        with open(path+'/results/2_containers/metrics_num_test_'+str(num_tests)+'_n_requests_'+str(n_requests)+'.pk', 'wb') as f:
                pickle.dump(cum_metrics,f)
        cum_metrics=[]
        n_requests+=1





















