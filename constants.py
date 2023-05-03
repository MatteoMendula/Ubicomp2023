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
IP_NANO = "10.42.0.42"
IP_PROMETHEUS_SERVER = "localhost"

PORT_FURCIFER_COMMAND_SERVER = "7999"
PORT_ENERGON_EXPORTER = "9877"
PORT_FURCIFER_EXPORTER = "9878"
PORT_PROMETHEUS_SERVER = "9090"
PORT_FURCIFER_NGINX = "8000"

ROUTE_TO_START_SAMPLING = "sample_camera_and_send_image_for_inference"
ROUTE_TO_STOP_SAMPLING = "stop_sampling"
ROUTE_TO_SET_INFERENCE_SERVER_URL = "set_server_url"
ROUTE_TO_EXCUTE_COMMAND = "execute_command"

SERVER_FULL_MODEL_ROUTE="furcifer_full_and_split_full"
SERVER_HEAD_MODEL_ROUTE="furcifer_full_and_split_head"

TIME_PER_SPOT_IN_SECONDS=60
NUMBER_SPOTS=8

LOGS_PATH='/home/sladrond/Documents/Research/Ubicomp_Experiments/github_experiments/Ubicomp2023/logs/'