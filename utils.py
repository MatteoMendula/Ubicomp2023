
def set_inference_server_url(ip, server_url):
    url = "http://{}:{}/{}".format(ip, PORT_FURCIFER_COMMAND_SERVER, ROUTE_TO_SET_INFERENCE_SERVER_URL)
    data = {
        "key": "ubicomp2023",
        "server_url": server_url
    }
    # Convert the data payload to JSON format
    payload = json.dumps(data)

    # Set the headers
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def start_sampling(ip, n_frames):
    url = "http://{}:{}/{}".format(ip, PORT_FURCIFER_COMMAND_SERVER, ROUTE_TO_START_SAMPLING)
    data = {
        "key": "ubicomp2023",
        "n_frames": n_frames,
    }
    # Convert the data payload to JSON format
    payload = json.dumps(data)

    # Set the headers
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def stop_sampling(ip):
    url = "http://{}:{}/{}".format(ip, PORT_FURCIFER_COMMAND_SERVER, ROUTE_TO_STOP_SAMPLING)
    data = {
        "key": "ubicomp2023",
    }
    # Convert the data payload to JSON format
    payload = json.dumps(data)

    # Set the headers
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def execute_command(ip, command):
    url = "http://{}:{}/{}".format(ip, PORT_FURCIFER_COMMAND_SERVER, ROUTE_TO_EXCUTE_COMMAND)
    data = {
        "key": "ubicomp2023",
        "command": command,
    }
    # Convert the data payload to JSON format
    payload = json.dumps(data)

    # Set the headers
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()