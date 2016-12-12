import sys

from master import *
from node import *
from reserve import *


def print_syntax():
    print("Syntax is: master|reserve|node <k8s url>")

if len(sys.argv) != 2:
    print_syntax()
    sys.exit()

mode = sys.argv[1]
url = sys.argv[2]

if mode == "master":
    setup_master()
elif mode == "reserve":
    setup_reserve()
elif mode == "node":
    setup_node()
else:
    print_syntax()
