import flask
from flask import Flask
from flask import render_template

from backend import data
app = Flask(__name__)


@app.route('/')
def home():
    args = tuple(get_args())
    # Ugly branching logic.
    if args == ():
        return render_template("index.html", advices=(), actions=data.actions)
    
    advices = []
    
    for arg in args:
        if arg == "":
            return render_template("index.html", advices=(), actions=data.actions)
        
    for arg, action in zip(args, data.actions):
        try:
            action.set_user_val(arg)
        except ValueError:
            return render_template("index.html", advices=(), actions=data.actions)

    fine = True
    for action in data.actions:
        if action.user_val > action.optimal:
            advices.append(action.advice)
            fine = False
    if fine:
        advices = ("You're okay!",)

    return render_template("index.html", advices=advices, actions=data.actions)


@app.route('/about')
def about():
    return render_template("about.html")


def get_args():
    for arg in flask.request.args.values():
        if arg is None:
            yield ""
        yield arg


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
