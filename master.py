import urllib.request


def setup_master():
    nodes = urllib.request.urlopen("http://localhost:8080/api/vi/nodes").read()

    print(nodes)

