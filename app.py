import flask
import json
import nlp

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    gen = flask.request.form.values()
    try:
        anything = tuple(gen)[0]
        action_type = nlp.get_type(anything)
        num = nlp.get_num(anything)

        with open('actions.json') as f:
            d = json.loads(f.read())
        optimal = d[action_type]['optimal']

        if num <= optimal:
            return flask.render_template('index.html', advice='Good')
        else:
            return flask.render_template('index.html', advice='Bad')
    except IndexError:
        # nothing in post
        pass
    except RuntimeError as e:
        print('error', anything, e)
        return flask.render_template('index.html', advice='We could not understand your input.')
    except TypeError as e:
        print('error', anything, e)
        return flask.render_template('index.html', advice='We could not understand your input.')

    return flask.render_template('index.html', advice='')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
