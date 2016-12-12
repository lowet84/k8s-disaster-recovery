import json
import urllib.request


def setup_master():
    nodes_json = urllib.request.urlopen("http://localhost:8080/api/v1/nodes").read()
    nodes = json.loads(nodes_json)

    print(nodes)

