import flask
import json
import nlp
import logging
from time import gmtime, strftime

app = flask.Flask(__name__)
logging.basicConfig(
    level=logging.DEBUG)

def log_ip(IP):
    with open('./IP-log.txt', mode='a', encoding='utf-8') as f:
        f.write('[{}] {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), IP))
        f.write('\n')

@app.route('/', methods=['GET', 'POST'])
def home():
    gen = flask.request.form.values()
    IP = None
    try:
        # Nginx request IP
        IP = flask.request.environ['HTTP_X_REAL_IP']
    except KeyError as e:
        # Flask HTTP server doesn't have HTTP_X_REAL_IP as a header
        IP = flask.request.environ['REMOTE_ADDR']

    log_ip(IP)

    try:
        anything = tuple(gen)[0]
        assert anything != ''

        action_type, num, unit = nlp.get_type_num_unit(anything)

        optimal = nlp.get_optimal(action_type, unit)

        if num <= optimal:
            logging.info(' IP: '+IP+' | input detected: %s -> %s', anything, 'good')
            return flask.render_template('index.html', advice='Good', desc="Your water consumption is not too much!")
        else:
            logging.info(' IP: '+IP+' | input detected: %s -> %s', anything, 'poor')
            return flask.render_template('index.html', advice='Poor', desc=f"Reduce your water consumption by "+str(float(num) - float(optimal))+" "+unit)
    except RuntimeError as e:
        logging.info(' IP: '+IP+' | input detected: %s -> %s', anything, e)
        return flask.render_template('index.html', advice='We could not understand your input.')
    except IndexError:
        # nothing in post
        return flask.render_template('index.html', advice='')
    except AssertionError:
        return flask.render_template('index.html', advice='')

@app.route('/crowdsource', methods=['GET', 'POST'])
def crowd():
    anything = tuple(flask.request.form.values())[0] if len(tuple(flask.request.form.values())) == 1 else None

    if anything is not None:
        append(anything)

    return flask.render_template('crowd.html')

CROWDFILE = 'crowd.txt'
def append(s):
    with open(CROWDFILE, 'a') as f:
        f.write(s)
        f.write('\n')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
