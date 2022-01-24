
from flask_restful import Resource
from flask import request

from sentiment_analysis import analyse_sentence


class SentimentController(Resource):

    def post(self):
        request_json = request.get_json(force=True, cache=False)
        sentence = request_json['sentence']
        is_from_twitter = request_json['twitter']
        analysis = analyse_sentence(sentence, is_from_twitter)

        return analysis
