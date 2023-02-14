# Logs Monitoring : Parse XML log file and export data to Grafana (and Prometheus) with Trend Apex One

Logs Monitoring : This project is used to parse an XML log file (here Trend Apex One log file) to export the data to Grafana using Prometheus.

In this project there are : :
  - a python script that parses the XML file but also serves as a Prometheus collector and exporter  
  - a config file prometheus.yml 
  - the requirements
  - an example of a Trend Apex One XML log file

## Prerequisites
Install [Python](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) (3.10).

Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

In Docker Desktop you need :
  - a container [Prometheus](https://prometheus.io/) (v2.29.2)
  - a container [Grafana](https://grafana.com/) (latest version)

```
docker run -d -p 9090:9090 --name prometheus -v /YOURWAY/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus:v2.29.2
docker run -d -p 3000:3000 --name grafana grafana/grafana:latest
```

## Installation

Start by installing the necessary libraries and modules.

```bash
pip install -r requirements.txt
```

Modify the **prometheus.yml** config file (/YOURWAY/prometheus.yml) to include your **IP** in the jobs. 

```
global:
  scrape_interval: 30s
  external_labels:
    monitor: 'node'
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['YOURIP:9090'] ## IP Address of the localhost. Match the port to your container port
  - job_name: 'apex_one'
    static_configs:
      - targets: ['YOURIP:9555'] ## IP Address of the localhost. Match the port to your container port
```

## Usage
Launch the Prometheus container and the Grafana container via Docker Desktop and then run the python script **parse_xml** in a Windows console.

```python
python api.py
```

To observe the metrics, go to : http://YOURIP:9555.

To create your dashboard go to : http://YOURIP:3000.

On Grafana, fill in the Prometheus data source with the address you have assigned (http://YOURIP:9090). 

## Documentation
[Make an exporter Prometheus in Python](https://www.dadall.info/article643/comment-prendre-un-peu-de-python-pour-faire-un-exporter-prometheus)

[The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)

## Contributions

All contributions are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)
