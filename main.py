import sys

from master import *
from node import *
from reserve import *


def print_syntax():
    print("Syntax is: master|reserve|node <k8s url>")

if len(sys.argv) != 3:
    print_syntax()
    sys.exit()

mode = sys.argv[1]
url = sys.argv[2]

if mode == "master":
    print("Setting up as master")
    setup_master()
elif mode == "reserve":
    print("Setting up as reserve")
    setup_reserve()
elif mode == "node":
    print("Setting up as node")
    setup_node()
else:
    print_syntax()
