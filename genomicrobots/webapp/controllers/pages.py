
from flask import render_template, Blueprint, request, jsonify, abort, Response, stream_with_context
from flask.json import dumps
from werkzeug.exceptions import NotFound

# from collections import Counter
# from operator import itemgetter
# import random
# import math
# import re

from ...analysis.example_analysis import *
from ...analysis.safesnpbot import *

web = Blueprint('genomicrobots', __name__)

#############################################################
# Routes for regular pages
#############################################################

robots = {
    'example': example_analysis,
    'safe_snp_bot': safe_snp_bot,
}


@web.route('/')
def home_page():
    return render_template('pages/home.html')


@web.route("/api/analysis", methods=['POST'])
def api_analysis():
    """ Runs genomic scan. Returns JSON PII-safe respones """

    robot_name = request.form.get("robot")
    print(robot_name)
    robot_function = robots.get(robot_name)
    if robot_function is None:
        abort(404)

    input_data = request.form.get("input_data")
    rslist = input_data.strip().split("\n")
    response = robot_function(rslist)

    if response is None:
        return jsonify({
            'error': 'An error occured while running the robot'
        })

    return jsonify({
        'response': response
    })
