class UserAction:
    def __init__(self, name: str, query: str, advice_format: str, optimal, unit):
        self.name = name
        self.user_val = None
        self.query = query
        self.advice_format = advice_format
        self.optimal = optimal
        self.unit = unit

    def set_user_val_on_cmdline(self):
        self.user_val = float(input("%s\n" % self.query))

    def set_user_val(self, user_val):
        self.user_val = float(user_val)

    @property
    def advice(self):
        return self.advice_format.format(self.optimal)