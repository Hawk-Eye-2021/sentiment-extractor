from flask import Flask
from flask_restful import Api
from controllers import helloController, sentimentController

from sentiment_analysis import init_classifier

init_classifier()

app = Flask(__name__)

api = Api(app)


api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(sentimentController.SentimentController, '/api/sentiment')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
