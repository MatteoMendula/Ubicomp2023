import time
import requests
from io import BytesIO
import json
import base64
import threading
import cv2

class User():
    def __init__(self, type_conenction, set_tasks, req_per_sec, url, start_time,duration, inference_metric_exporter) :
        self.type_connection=type_conenction
        self.set_tasks=set_tasks
        self.req_per_sec=req_per_sec
        self.url = url
        self.start_time=start_time
        self.duration=duration
        self.inference_metric_exporter=inference_metric_exporter
        self.cap = cv2.VideoCapture(0)

    def send_async(self,url, json_data, headers, results):
        response = requests.post(url, data=json_data, headers=headers, timeout=10)
        results.append(response.text)
    
    def start(self):
        def send_req_per_second():
            ret, frame = self.cap.read()
            retval, buffer = cv2.imencode('.jpg', frame)
            # img_file = "000000001675.jpg"
            # with open(img_file, "rb") as f:
            #     img_data = f.read()
            # img_bytes = BytesIO(frame)
            img_base64 = base64.b64encode(buffer).decode('utf-8')
            headers = {"Content-type": "application/json"}
            data = {
                "type_task": "IMAGE_CLASS",
                "image": img_base64
            }
            json_data = json.dumps(data)


            start_time = time.time()
            threads = [None] * self.req_per_sec
            results = []
            for i in range(len(threads)):
                threads[i] = threading.Thread(target=self.send_async, args=(self.url, json_data, headers, results,))
                threads[i].start()
            for i in range(len(threads)):
                threads[i].join()
            print("results", " ".join(results))
            end_time = time.time()
            time_in_ms = (end_time - start_time) * 1000

            self.inference_metric_exporter.set_latency(time_in_ms)

            print("Time interval in milliseconds:", time_in_ms)
            print(len(results))
            if (time.time() < self.start_time+self.duration):
                time.sleep(1)
                send_req_per_second()  
            
        send_req_per_second()