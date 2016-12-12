import json
import urllib.request


def setup_master():
    nodes = json.loads(urllib.request.urlopen("http://localhost:8080/api/v1/nodes").read())

    print(nodes)

