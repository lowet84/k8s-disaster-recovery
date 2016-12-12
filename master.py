import codecs
import json
import urllib.request

def get_storage():
    nodes_json = urllib.request.urlopen("http://localhost:8080/api/v1/nodes")
    reader = codecs.getreader("utf-8")
    data = json.load(reader(nodes_json))

    storage = []

    for node in data['items']:
        hostname = node['metadata']['labels']['kubernetes.io/hostname']
        if 'role' in node['metadata']['labels']:
            role = node['metadata']['labels']['role']
        else:
            role = None

        if role == 'storage':
            storage.append(hostname)

    return storage

def setup_master():

    storage = get_storage()
    print(storage)
