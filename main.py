from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    msg = ""

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        msg = "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        msg = "negative"

    else:
        msg = "neutral"

    return msg + " " + str(sentiment_dict['compound'])


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/text', methods=['GET', 'POST'])
def text():
    text = request.form['text']
    sentiment = sentiment_scores(text)
    return sentiment


app.run(debug=True)
