import flask
import nlp

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    gen = flask.request.form.values()
    try:
        anything = tuple(gen)[0]
    except:
        return flask.render_template('index.html')
    print(anything, nlp.return_action_type(anything))
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
