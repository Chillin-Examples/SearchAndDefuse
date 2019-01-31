###############################################################
###                                                         ###
###     Don't forget to set directories in configs.json     ###
###       * set code_base_directory to the address where    ###
###         your whole game folder is.                      ###
###       * set monitor_directory to your monitor folder    ###
###                                                         ###
###############################################################

import os
import threading
import time
import json
import platform


configs = json.loads(open(("configs.json"), "r").read())
monitor_directory = configs["monitor_directory"]
code_base_directory = configs["code_base_directory"]

if platform.system() == 'Windows':
    monitor_exe = 'ChillinMonitor2.exe'
elif platform.system() == 'Linux':
    monitor_exe = './ChillinMonitor2.x86_64'
elif platform.system() == 'Darwin':
    monitor_exe = 'open ChillinMonitor2.app'


class RunMonitor(threading.Thread):
    def run(self):
        print("Running Monitor...")
        os.system('cd {} && {}'.format(monitor_directory, monitor_exe))


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
    if configs["run_monitor"]:
        run_monitor.start()
        time.sleep(2)
    if configs["run_python_client"]:
        run_client.start()
        time.sleep(1)
    if configs["run_python_random_client"]:
        run_random_client.start()
