class Sticks:
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        self.players[name] = []

    def take_sticks(self, name, sticks_taken):
        if sticks_taken < 4 and sticks_taken > 0:
            self.players[name].append(sticks_taken)
            if self.get_sticks_remaining() > 0:
                return f"{name} takes {str(sticks_taken)}"
            else:
                return f"{name} takes {str(sticks_taken)} - {name} Wins!"
        else:
            return 'Players can only take between 1 and 3 sticks in a turn'

    def get_sticks_remaining(self):
        total_sticks = 21
        for value in self.players.values():
            total_sticks -= sum(value)
        return total_sticks
