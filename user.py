import time
import requests
from io import BytesIO
import json
import base64
import threading

class User():
    def __init__(self,number_request,type_conenction, set_tasks, req_per_sec, ip, port, route, start_time,duration, logger = None) :
        self.number_request=number_request
        self.type_connection=type_conenction
        self.set_tasks=set_tasks
        self.req_per_sec=req_per_sec
        self.ip = ip
        self.port = port
        self.route = route
        self.start_time=start_time
        self.duration=duration
        self.latencies=[]
        self.logger = logger

    def send_async(self,url, json_data, headers, results):
        response = requests.post(url, data=json_data, headers=headers, timeout=10)
        results.append(response.text)

    def get_latencies(self):
        print(self.latencies)
        return self.latencies
    
    def start(self):
        img_file = "000000001675.jpg"
        with open(img_file, "rb") as f:
            img_data = f.read()
        img_bytes = BytesIO(img_data)
        img_base64 = base64.b64encode(img_data).decode('utf-8')
        url = "http://{}:{}/{}".format(self.ip, self.port, self.route)
        headers = {"Content-type": "application/json"}
        data = {
            "type_task": "IMAGE_CLASS",
            "image": img_base64
        }
        json_data = json.dumps(data)
        def send_req_per_second():
            global latency

            start_time = time.time()
            threads = [None] * self.req_per_sec
            results = []
            for i in range(len(threads)):
                threads[i] = threading.Thread(target=self.send_async, args=(url, json_data, headers, results,))
                threads[i].start()
            for i in range(len(threads)):
                threads[i].join()
            print(" ".join(results))
            end_time = time.time()
            time_in_ms = (end_time - start_time) * 1000
            
            latency = time_in_ms

            self.latencies.append(time_in_ms)
            print("Time interval in milliseconds:", time_in_ms)
            print(len(results))
            if (time.time() < self.start_time+self.duration):
                time.sleep(1)
                send_req_per_second()  
            return self.latencies 
            
        self.latencies=send_req_per_second()