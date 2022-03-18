
from flask_restful import Resource
from flask import request

from sentiment_analysis import analyse_sentence


class SentimentController(Resource):

    def post(self):
        request_json = request.get_json()
        extraction = request_json['extraction']
        analysis = analyse_sentence(extraction)

        return analysis
