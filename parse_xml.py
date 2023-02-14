import xml.etree.ElementTree as ET

from prometheus_client import start_http_server, REGISTRY 
from prometheus_client.core import GaugeMetricFamily
from time import sleep       


class Collector(object): 
    def __init__(self):   
        self.url = 'http://schemas.microsoft.com/win/2004/08/events/event' # Very important for namespace (xmlns), but it depends of your XML file                                
        pass

    def collect(self):
        tree = ET.parse('YOURXML.xml') # Change the file to your xml file
        root = tree.getroot()

        metric = GaugeMetricFamily('EventID', "Number of virus and infected computer(s)", labels=['count_virus', 'count_computer'])

        for event in root.findall('{' + self.url + '}Event') :
            EventData = event.find('{' + self.url + '}EventData')
            Data = EventData.find('{' + self.url + '}Data').text
            virus = Data.split(": ")[1] # We have to split to get only numbers we want without text arround
            count_virus = virus.split("\n")[0]
            computer = Data.split(": ")[2]
            count_computer = computer.split("\n")[0]
            EventRecordID = event.find('{' + self.url + '}System').find('{' + self.url + '}EventRecordID').text
            
            metric.add_metric(labels=[count_virus, count_computer], value=EventRecordID)

        yield metric

if __name__ == "__main__":
    start_http_server(9555)     
    REGISTRY.register(Collector())
    while True: sleep(10)




