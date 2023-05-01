# Ubicomp2023

## Experiment1 scalability to run setup
- connect to the xavier with ssh
- run inside the Furcifer repository ``sudo docker-compose -f _jetson_docker-compose.yml up``
- run inside the EnergonPrometheuesExporter ``sudo python3 prometheus_exporter.py``
- set the targets prometheus server yml file ``ip_xavier:9877`` and ``localhost:9878``
- run on you laptop a Prometheus server
- run the test_scalability.py file inside the Ubicomp2023 repository ``python test_scalability.py --url http://ip_xavier:8000/furcifer_efficientnet_b0``