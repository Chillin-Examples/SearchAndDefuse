###############################################################
###                                                         ###
###     don't forget to set directories in configs.json     ###
###                                                         ###
###############################################################
import os
import threading
import time
import json

configs = json.loads(open(("configs.json"), "r").read())
monitor_directory = configs["monitor_directory"]
code_base_directory = configs["code_base_directory"]


class RunMonitor(threading.Thread):
    def run(self):
        print("Running Monitor...")
        os.system('cd {} && ChillinMonitor2.exe'.format(monitor_directory))


class RunServer(threading.Thread):
    def run(self):
        print("Running Server...")
        os.system('cd {}PythonServer && python main.py'.format(code_base_directory))


class RunClient(threading.Thread):
    def run(self):
        print("Running Client...")
        os.system('cd {}PythonClient && python main.py'.format(code_base_directory))


class RunRandomClient(threading.Thread):
    def run(self):
        print("Running Random Client...")
        os.system('cd {}PythonRandomClient && python main.py'.format(code_base_directory))


if __name__ == '__main__':
    run_monitor = RunMonitor(name="RunMonitor")
    run_server = RunServer(name="RunServer")
    run_random_client = RunRandomClient(name="RunRandomClient")
    run_client = RunClient(name="RunClient")

    run_server.start()
    time.sleep(1)
    run_monitor.start()
    time.sleep(2)
    run_client.start()
    time.sleep(1)
    run_random_client.start()
