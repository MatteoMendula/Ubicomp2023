from prometheus_client import start_http_server, Gauge, Info

class FurciferDataExporter:
    def __init__(self, app_port=9878, polling_interval_seconds=0.05):
        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds
        self.device_info = Info("furcifer_data_export_info", "Device info")
        self.latency = Gauge("furcifer_latency_ms", "Current latency in milli seconds")
        self.init_server()

    def init_server(self):
        self.device_info.info(
            {
                "app_port": self.app_port.detected_model, 
                "polling_interval_seconds": self.polling_interval_seconds, 
            }
        )
        self.latency.set(-1)
        start_http_server(self.app_port)

    def set_latency(self, latency):
        self.latency.set(latency)