# Constants to avoid errors from mistyping strings

# Things that consume water
FLUSH = 'flush'
SHOWER = 'shower'
DRINK = 'drink'

TIMES = 'times'
MINUTES = 'minutes'
LITRES = 'litres'

# The optimal amounts

# https://www.pub.gov.sg/Documents/PUB_7%20Good%20water%20saving%20habits_FA_LORES.pdf

optimal = {
    FLUSH: 8,
    SHOWER: 5,
    DRINK: 2.25,
}


class UserAction:
    def __init__(self, action, query, advice_format, unit):
        self.action = action
        self.user_val = None
        self.optimal = self._get_optimal_val()
        self.query = query
        self.advice_format = advice_format
        self.unit = unit

    def _get_optimal_val(self):
        return optimal[self.action]

    def get_user_val(self):
        self.user_val = float(input("%s\n" % self.query))


actions = (
    UserAction(FLUSH,
               'How many times do you flush your toilet per day?',
               'Try flushing the toilet {} times tomorrow.',
               TIMES),
    UserAction(SHOWER,
               'How much time do you usually spend in the shower?',
               'Shorten your shower time to {} minutes in the future.',
               MINUTES),
    UserAction(DRINK,
               'How many litres of water do you drink per day?',
               'Unless you perspire a lot, drink {} litres of water tomorrow.',
               LITRES),
)