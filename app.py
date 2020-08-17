import flask
from flask import Flask
from flask import render_template

from backend.read import actions
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    args = tuple(get_args())
    # Ugly branching logic.
    if args == ():
        return render_template('index.html', advices=(), actions=actions)
    
    advices = []
    
    if '' in args:
        return render_template('index.html', advices=(), actions=actions)
        
    for arg, action in zip(args, actions):
        try:
            action.set_user_val(arg)
        except ValueError:
            return render_template('index.html', advices=(), actions=actions)

    fine = True
    for action in actions:
        if action.user_val > action.optimal:
            advices.append(action.advice)
            fine = False
    if fine:
        advices = ('You\'re okay!',)

    return render_template('index.html', advices=advices, actions=actions)


@app.errorhandler(404)
def func404(e):
    return render_template('404.html')


def get_args():
    for arg in flask.request.form.values():
        if arg is None:
            yield ''
        yield arg


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
