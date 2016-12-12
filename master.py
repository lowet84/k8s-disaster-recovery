import codecs
import json
import urllib.request

def setup_master():
    nodes_json = urllib.request.urlopen("http://localhost:8080/api/v1/nodes")
    reader = codecs.getreader("utf-8")
    data = json.load(reader(nodes_json))

    # with open('nodes.txt') as data_file:
    #     data = json.load(data_file)

    storages = []

    for node in data['items']:
        hostname = node['metadata']['labels']['kubernetes.io/hostname']
        if 'role' in node['metadata']['labels']:
            role = node['metadata']['labels']['role']
        else:
            role = None

        if role == 'storage':
            storages.append(hostname)

    print(storages)
