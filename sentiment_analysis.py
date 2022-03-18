from googletrans import Translator
import aspect_based_sentiment_analysis as absa

nlp = None
translator = None

sentiment_map = {
    absa.Sentiment.neutral: "neutral",
    absa.Sentiment.negative: "negative",
    absa.Sentiment.positive: "positive"
}


def init_classifier():
    global nlp
    global translator
    translator = Translator()
    nlp = absa.load()


def analyse_sentence(extraction):

    global sentiment_map

    print(extraction)
    translation = {"title": extraction['title'], "translation": translator.translate(extraction['title'], dest='en').text, "entities": extraction['entities']}
    analysis = nlp(translation['translation'], aspects=translation['entities'])

    sentiments = {}
    for entity in translation['entities']:
        sentiments[entity] = sentiment_map[analysis[entity].sentiment]

    return {"title": translation['title'], "entities": translation['entities'], "sentiments": sentiments}
