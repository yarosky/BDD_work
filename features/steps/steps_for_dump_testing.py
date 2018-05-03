# -- FILE: features/steps/example_steps.py
import os
import subprocess
import __main__
from behave import *


@given('Server Address {SERV}')
def step_impl(context, SERV):
    global args
    args = []
    context.serv = str(SERV)
    args.append("-a")
    args.append(context.serv)



@given('Server port {PORT}')
def step_impl(context, PORT):
    context.port = str(PORT)
    args.append("-p")
    args.append(context.port)


@given('Output file {OUTPUT}')
def step_impl(context, OUTPUT):
    context.OUTPUT = OUTPUT
    args.append("-o")
    args.append(context.OUTPUT)


@when("CLI is started with args")
def step_impl(context):
    arg = " "
    for i in range(len(args)):
        arg += " " + str(args[i])
    launch_main_args = "python __main__.py" + str(arg)
    print("Launch CLI tool like: " + launch_main_args)

    try:
        context.launch = subprocess.Popen(launch_main_args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, universal_newlines=True)
        context.lines = []
        del arg
        del launch_main_args

        for line in context.launch.stdout:
            context.lines.append(line)
    except Exception as e:
        context.ex = e
        assert e


@then("Output file is created and should contain some text")
def step_impl(context):
    path_file = os.path.isfile(context.OUTPUT)
    print("Expected path to output file: " + str(context.OUTPUT))
    assert path_file == True, "Output file was not created"
    assert os.path.getsize(context.OUTPUT) != 0, "Output file is empty"

@then("[WinError {ERRCODE}]")
def step_impl(context, ERRCODE):
    stdout_console = context.lines.pop()
    error = stdout_console.split(":")[0]
    print("Expected error: " + str(stdout_console))
    assert "ERROR" == str(error), str(stdout_console)


@given(u'arguments not exist')
def step_impl(context):
    pass


@when(u'CLI is started without args')
def step_impl(context):
    launch_main = "python __main__.py"
    try:
        context.launch = subprocess.Popen(launch_main, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, universal_newlines=True)
        context.lines = []
        for line in context.launch.stdout:
            context.lines.append(line)
    except Exception as e:
        context.ex = e
        assert e

@then(u'Help appears')
def step_impl(context):
    stdout_console = context.lines.pop(0)
    error = stdout_console.split(' ')[1]
    print("Expected output of HELP: " + stdout_console)
    assert "BDD_Task" == error, stdout_console


