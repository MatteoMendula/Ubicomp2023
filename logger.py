import time
from urllib.request import urlopen
import json
import threading

class Logger(threading.Thread):
    def __init__(self, start_time, duration, url, metrics) :
        super(Logger, self).__init__()
        self.daemon = True 
        self.start_time=start_time
        self.duration=duration
        self.url=url
        self.metrics=metrics
        self.stored_metrics={}

        # http://localhost:9090/api/v1/query?query={__name__=~%22energon_cpu_in_power_mW|energon_gpu_in_power_mW|energon_cpu_total_usage_percentage|energon_gpu_total_usage_percentage|energon_ram_used_percentage|furcifer_latency_ms%22,%20instance=~%22localhost:9877%22}
        self.query_url = url + "{" + "__name__=~'{}'".format("|".join(metrics)) + "}"

        for e in self.metrics:
            self.stored_metrics[e]=[]
        self.stored_metrics['timestamp']=[]

    def find_metric(self, obj, metric):
        result = {}
        if len(obj["data"]["result"]) == 0:
            return result
        for m in obj["data"]["result"]:
            if m["metric"]["__name__"] == metric:
                result["timestamp"] = m["value"][0]
                result["value"] = m["value"][1]
                break
        return result

    def run(self):
        while(time.time() < self.start_time+self.duration):
            response = urlopen(self.query_url)
            data_json = json.loads(response.read())
            is_timestamp_saved = False
            for metric in self.metrics:
                try:
                    metric_query_result_firtered = self.find_metric(data_json, metric)
                    print("-----------", metric)
                    print("data_json", metric_query_result_firtered)
                    value = metric_query_result_firtered["value"]
                    timestamp = metric_query_result_firtered["timestamp"]
                    self.stored_metrics[metric].append(float(value))
                    if is_timestamp_saved == False:
                        print("pushing timestamp", len(self.stored_metrics['timestamp']))
                        print("len metric", len(self.stored_metrics[metric]))
                        self.stored_metrics['timestamp'].append(timestamp)
                        is_timestamp_saved = True
                except Exception as e:
                    print("Couldn't get the data, please check the server", e)

            time.sleep(1)

    def get_metrics(self,start_time,end_time):
        print("len self.stored_metrics['timestamp']", len(self.stored_metrics['timestamp']))
        for metric in self.metrics:
            print("len self.stored_metrics[{}]".format(metric), len(self.stored_metrics[metric]))
        
        indexes = [idx for idx, element in enumerate(self.stored_metrics['timestamp']) if (element >= start_time and element<=end_time)]
        for metric in self.metrics:
            self.stored_metrics[metric]=[self.stored_metrics[metric][j] for j in indexes]
        self.stored_metrics['timestamp'] = [self.stored_metrics['timestamp'][j] for j in indexes]
        return self.stored_metrics   