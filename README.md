# Aquatify
    python3 cmdrun.py
or,

    python3 app.py  # flask app on localhost

### Todo
- Make suggestions more specific
- Write more suggestions
- Allow skipping of some questions in the web page

### Idea 23/10/2020
The user types in any sentence related to their consumption of water,
for example:
- "I usually drink 3 litres of water a day"
- "i go to the urinal 4 times a day"
- or anything that's not too cryptic.

The backend then processes their sentence and gets several pieces of data, including:
- the thing that they're using to consume water, such as toilet flushing, showering, or drinking
- the appropriate unit, such as amount of toilet flushes, minutes of showering time, or litres respectively

It then does what it already does (23/10/2020), which is send the optimal amount of that consumption
type if the user consumes more than the optimal amount.

This is a lot better than the current user interaction model, which dumps them a bunch of forms to answer.