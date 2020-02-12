"""
Script start or stops or restarts Acronis services
Available options: /start, /stop, /restart
Usage example:
> scriptName /start
"""

import os
import sys

SERVICES = ["HvVmWatcher", "MMS", "AMS", "AcrMngSrv", "AcronisMonitoringService", "AcronisAgent", "ARSM", "AcrSch2Svc",
            "ASM", "StorageNode", "AcronisZmqGw", "CatalogBrowserService"]


def serviceAction(action):
    for serviceName in SERVICES:
        os.system("net " + action + " " + serviceName + " /y")
    print("Done!")

try:
    if sys.argv[1] == "/start":
        serviceAction("Start")
    elif sys.argv[1] == "/stop":
        serviceAction("Stop")
    elif sys.argv[1] == "/restart":
        serviceAction("Stop")
        serviceAction("Start")
    elif sys.argv[1] == "/help":
        print("Script start or stops or restarts Acronis services \n"
              "Available options: /start, /stop, /restart \n"
              "Usage example:\n"
              "> scriptName /start\n")
except Exception:
    print("Wrong option. Usage: scriptName [option]. Options: /start, /stop, /restart, /help")
