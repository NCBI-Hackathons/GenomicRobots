
from flask import render_template, Blueprint, request, jsonify, abort, Response, stream_with_context
from flask.json import dumps
from werkzeug.exceptions import NotFound

# from collections import Counter
# from operator import itemgetter
# import random
# import math
# import re

from ...analysis.example_analysis import *

web = Blueprint('mutagene', __name__)

#############################################################
# Routes for regular pages
#############################################################


@web.route('/')
def home_page():
    return render_template('pages/home.html')


@web.route("/api/example_analysis", methods=['POST'])
def api_example():
    """ Runs genomic scan. Returns JSON PII-safe respones """

    input_data = request.form.get("input_data")

    response = example_analysis(input_data)

    return jsonify({
        'response': response
    })
