import time
from sys import argv
import time
import numpy as np
import argparse

from user import User
from logger import Logger
from inference_metrics_exporter import InferenceMetricsExporter

# experiment settings
parser = argparse.ArgumentParser()

parser.add_argument(
    "-p",
    "--port",
    nargs="?",
    default=8000,
    type=int,
    help="Port of the server",
)
parser.add_argument(
    "-i",
    "--ip",
    nargs="?",
    default="localhost",
    type=str,
    help="IP of the server",
)
parser.add_argument(
    "-r",
    "--route",
    nargs="?",
    default="furcifer_efficientnet_b0",
    type=str,
    help="Route of the server",
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
    "-u",
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
metrics.append("furcifer_latency_avg_ms")
metrics.append("furcifer_latency_var_ms")

if __name__ == "__main__":

    start_time_user = time.time()

    duration_user = args.duration
    num_tests = args.n_tests
    prometheus_server_url = args.prometheus_server_url
    ip = args.ip
    port = args.port
    route = args.route

    inference_metric_exporter = InferenceMetricsExporter()
    inference_metric_exporter.setDaemon(True)
    inference_metric_exporter.start()

    duration_metrics = (duration_user * num_tests) + 3
    log_metrics = Logger(time.time(), duration_metrics, prometheus_server_url, metrics)
    log_metrics.setDaemon(True)
    log_metrics.start()

    avg_var_metrics={}
    n_requests = 1
    for j in range(num_tests):
        print("Testing "+ str(n_requests) + " requests per second")
        start_time_user=time.time()
        user_1=User(10, 'BAD',set(), n_requests, ip, port, route, start_time_user, duration_user, log_metrics)
        user_1.start()
    
        print("Getting the metrics ")
        results_metrics=log_metrics.get_metrics(start_time_user,start_time_user+duration_user)

        temp_dict_avg={}
        temp_dict_var={}
        for i in range(len(metrics)):
            temp_dict_avg[metrics[i]]=sum(results_metrics[metrics[i]])/len(results_metrics[metrics[i]])
            temp_dict_var[metrics[i]]=np.var(results_metrics[metrics[i]])
        temp_dict_avg['latency']=sum(user_1.get_latencies())/len(user_1.get_latencies())
        temp_dict_var['latency']=np.var(user_1.get_latencies())

        avg_var_metrics[j]={'avg':temp_dict_avg, 'var':temp_dict_var}
        print(avg_var_metrics)
        
        log_metrics = user_1.logger
        
        del user_1
        n_requests+=1





















