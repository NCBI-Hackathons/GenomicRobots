#!/usr/bin/env python
import os
from flask_script import Manager, prompt_bool
from .analysis import *


PATH = os.path.abspath(os.path.dirname(__file__)) + "/data/"


def get_command_manager(app):
    manager = Manager(app, usage="Genomic Robots web server maintenance")

    @manager.command
    def hello():
        "Hello"
        print("OK")

    @manager.command
    def runsimple():
        "Run webserver"
        app.run(processes=5, threaded=False)

    return manager
