from prometheus_client import start_http_server, Gauge, Info
import threading

class InferenceMetricsExporter(threading.Thread):
    def __init__(self, app_port=9878, polling_interval_seconds=0.05):
        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds
        self.device_info = Info("furcifer_data_export_info", "Device info")
        self.latency_average = Gauge("furcifer_latency_avg_ms", "Average latency in milli seconds")
        self.latency_variance = Gauge("furcifer_latency_var_ms", "Variance of latency in milli seconds")
        self.init_server()

    def init_server(self):
        self.device_info.info(
            {
                "app_port": self.app_port.detected_model, 
                "polling_interval_seconds": self.polling_interval_seconds, 
            }
        )
        self.latency_avg.set(-1)
        start_http_server(self.app_port)

    def set_avg_latency(self, avg):
        self.latency_average.set(avg)

    def set_var_latency(self, var):
        self.latency_variance.set(var)