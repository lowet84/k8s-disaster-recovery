import codecs
import json
import urllib.request


def setup_master():
    nodes_json = urllib.request.urlopen("http://localhost:8080/api/v1/nodes").read()
    reader = codecs.getreader("utf-8")
    nodes = json.loads(reader(nodes_json))

    print(nodes)

