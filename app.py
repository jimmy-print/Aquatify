import flask
import json
import nlp
import logging

app = flask.Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def home():
    gen = flask.request.form.values()
    try:
        anything = tuple(gen)[0]
        assert anything != ''
        action_type = nlp.get_type(anything)
        num = nlp.get_num(anything)

        with open('actions.json') as f:
            d = json.loads(f.read())
        optimal = d[action_type]['optimal']

        if num <= optimal:
            logging.info('input: %s -> %s', anything, 'good')
            return flask.render_template('index.html', advice='Good')
        else:
            logging.info('input: %s -> %s', anything, 'bad')
            return flask.render_template('index.html', advice='Bad')
    except RuntimeError as e:
        logging.warning('input: %s -> %s', anything, e)
        return flask.render_template('index.html', advice='We could not understand your input.')
    except ValueError as e:
        logging.warning('input: %s -> %s', anything, e)
        return flask.render_template('index.html', advice='We could not understand your input.')
    except IndexError:
        # nothing in post
        return flask.render_template('index.html', advice='')
    except AssertionError:
        return flask.render_template('index.html', advice='')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
