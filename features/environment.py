# -- FILE: features/environment.py
from behave import *
import subprocess
import os


def before_scenario(context, scenario):
    context.server = subprocess.Popen('python server_socket.py')



def after_scenario(context, scenario):
    context.server.terminate()
    try:
        os.remove(context.OUTPUT)
    except:
        pass