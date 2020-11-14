import flask
import json
import nlp
import logging

app = flask.Flask(__name__)
logging.basicConfig(
    level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def home():
    gen = flask.request.form.values()
    try:
        anything = tuple(gen)[0]
        assert anything != ''
        action_type = nlp.get_type(anything)
        num = (nlp.get_num(anything))

        with open('actions.json') as f:
            d = json.loads(f.read())
        optimal = (d[action_type]['optimal'])


        if num <= optimal:
            logging.info('input: %s -> %s', anything, 'good')
            return flask.render_template('index.html', advice='Good', desc="Your consumption is not too much!")
        else:
            logging.info('input: %s -> %s', anything, 'bad')
            return flask.render_template('index.html', advice='Bad', desc="Reduce your consumption by "+str(float(num) - float(optimal)))
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
