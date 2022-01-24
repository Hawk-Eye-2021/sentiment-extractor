from pysentimiento import create_analyzer
from pysentimiento.preprocessing import preprocess_tweet


analyzer = None


def init_classifier():
    global analyzer
    analyzer = create_analyzer(task="sentiment", lang="es")


def analyse_sentence(sentence, is_from_twitter):
    aux_sentence = sentence

    if is_from_twitter:
        aux_sentence = preprocess_tweet(sentence)
    prediction = analyzer.predict(aux_sentence)
    output = prediction.output

    if output == 'NEG':
        return 'negative'
    if output == 'NEU':
        return 'neutral'
    if output == 'POS':
        return 'positive'

    return prediction.output
