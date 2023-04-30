import time
from urllib.request import urlopen
import json
import threading

class Logger(threading.Thread):
    def __init__(self, start_time, duration, url, metrics) :
        super(Logger, self).__init__()
        self.start_time=start_time
        self.duration=duration
        self.url=url
        self.metrics=metrics
        self.stored_metrics={}

        for e in self.metrics:
            self.stored_metrics[e]=[]
        self.stored_metrics['timestamp']=[]

    def run(self):
        while(time.time() < self.start_time+self.duration):
            self.stored_metrics['timestamp'].append(time.time())
            for metric in self.metrics:
                new_url = self.url + metric
                response = urlopen(new_url)
                data_json = json.loads(response.read())
                try:
                    val=data_json['data']['result'][0]['value'][1]
                    self.stored_metrics[metric].append(float(val))
                except Exception as e:
                    print("Couldn't get the data, please check the server", e)

    def get_metrics(self,start_time,end_time):
        print("len self.stored_metrics['timestamp']", len(self.stored_metrics['timestamp']))
        for metric in self.metrics:
            print("len self.stored_metrics[metric]", len(self.stored_metrics[metric]))
        
        indexes = [idx for idx, element in enumerate(self.stored_metrics['timestamp']) if (element >= start_time and element<=end_time)]
        for metric in self.metrics:
            self.stored_metrics[metric]=[self.stored_metrics[metric][j] for j in indexes]
        self.stored_metrics['timestamp'] = [self.stored_metrics['timestamp'][j] for j in indexes]
        return self.stored_metrics   