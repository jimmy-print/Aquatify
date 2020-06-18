import flask
from flask import Flask
from flask import render_template

from backend import data
app = Flask(__name__)


@app.route('/')
def home():
    args = tuple(get_args())
    advices = []
    # Ugly branching logic.
    for arg in args:
        if arg == "":
            break
    else:
        for arg, action in zip(args, data.actions):
            try:
                action.set_user_val(arg)
            except ValueError:
                break;
        else:
            for action in data.actions:
                if action.user_val > action.optimal:
                    advices.append(action.advice)
    return render_template("index.html", advices=advices)


@app.route('/about')
def about():
    return render_template("about.html")


def get_args():
    args = [
        flask.request.args.get("flush"),
        flask.request.args.get("shower"),
        flask.request.args.get("drink"),
    ]
    for i, arg in enumerate(args):
        if arg is None:
            yield ""
        yield arg


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
