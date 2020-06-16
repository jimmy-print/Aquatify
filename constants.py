# Constants to avoid errors from mistyping strings

# Things that consume water
FLUSH = 'flush'
SHOWER = 'shower'
DRINK = 'drink'

TIMES = 'times'
MINUTES = 'minutes'
LITRES = 'litres'

actions = FLUSH, SHOWER, DRINK
queries = (
    'How many times do you flush your toilet per day?',
    'How much time do you usually spend in the shower?',
    'How many litres of water do you drink per day?',
)
units = TIMES, MINUTES, LITRES
should = (
    NotImplemented,
    'You should take shorter showers.',
    'You should drink less water, unless you need to drink more.'
)