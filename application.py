import flask
import json
import nlp
import logging
from time import gmtime, strftime

app = flask.Flask(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename='log.log',
    format='%(levelname)s:%(name)s:%(asctime)s:%(message)s')

@app.route('/', methods=['GET', 'POST'])
def home():
    gen = flask.request.form.values()

    try:
        # Nginx request IP
        IP = flask.request.environ['HTTP_X_REAL_IP']
    except KeyError as e:
        # Flask HTTP server doesn't have HTTP_X_REAL_IP as a header
        logging.debug('IP exception %s', e)
        IP = flask.request.environ['REMOTE_ADDR']

    logging.info(IP)

    try:
        anything = tuple(gen)[0]
    except IndexError:
        # nothing in post
        return flask.render_template('index.html', advice='')

    try:
        assert anything != ''

        action_type, num, unit = nlp.get_type_num_unit(anything)

        optimal = nlp.get_optimal(action_type, unit)

        if num <= optimal:
            logging.info('input detected: %s -> %s', anything, 'good')
            return flask.render_template('index.html', advice='Good', desc="Your water consumption is not too much!")
        else:
            logging.info('input detected: %s -> %s', anything, 'poor')
            return flask.render_template('index.html', advice='Poor', desc=f"Reduce your water consumption by "+str(float(num) - float(optimal))+" "+unit)
    except RuntimeError as e:
        logging.info('input detected: %s -> %s', anything, e)
        return flask.render_template('index.html', advice='Please rephrase your input.')

    except AssertionError:
        return flask.render_template('index.html', advice='')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
