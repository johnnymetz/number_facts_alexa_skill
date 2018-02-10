from flask import Flask, render_template
from flask_ask import Ask, statement, question
import requests
import logging

app = Flask(__name__)
ask = Ask(app, '/')
# logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    reprompt_text = render_template('welcome_reprompt')
    return question(welcome_text).reprompt(reprompt_text)


@ask.intent('RandomNumberFactIntent')
def random_fact():
    url = 'http://numbersapi.com/random/trivia'
    r = requests.get(url)
    fact = r.text
    return statement(speech=fact).simple_card(title='Number Facts', content=fact)


@ask.intent('SpecifiedNumberFactIntent', convert={'number': int})
def specified_fact(number):
    if number is None:
        repeat_text = render_template('number_error')
        return question(repeat_text).reprompt(repeat_text)
    url = f'http://numbersapi.com/{number}'
    r = requests.get(url)
    fact = r.text
    return statement(speech=fact).simple_card(title='Number Facts', content=fact)


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement(render_template('bye'))


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement(render_template('bye'))


@ask.intent('AMAZON.HelpIntent')
def help():
    return question(render_template('help'))


@ask.session_ended
def session_ended():
    return '{}', 200


if __name__ == '__main__':
    app.run(debug=True)
