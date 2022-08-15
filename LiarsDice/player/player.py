from random import choice


class Player:
    INITIAL_DICES = [None, None, None, None, None]
    PLAYER_HOLDER = {}

    def __init__(self, name):
        self.name = name
        self.dices = self.INITIAL_DICES

    def add_player(self):
        if self.name in self.PLAYER_HOLDER:
            return
        self.PLAYER_HOLDER[self.name] = self.INITIAL_DICES


dice_holder = {}
digits_of_dice = [1, 2, 3, 4, 5, 6]


class ThrowTheDice:

    @staticmethod
    def throw_the_dices():
        for name, dices in Player.PLAYER_HOLDER.items():
            dice_holder[name] = []
            for _ in dices:
                dice_num = choice(digits_of_dice)
                dice_holder[name].append(dice_num)

        return dice_holder


class CountCurrentDices:

    @staticmethod
    def count_current_dices():
        counter = 0
        for dices in Player.PLAYER_HOLDER.values():
            for _ in dices:
                counter += 1

        return counter


player1 = Player('Gosho')
player2 = Player('Maria')
player3 = Player('Pesho')
player4 = Player('Dido')

player1.add_player()
player2.add_player()
player3.add_player()
player4.add_player()

print(ThrowTheDice.throw_the_dices())
print(CountCurrentDices.count_current_dices())


class Bid:

    @staticmethod
    def bid():
        current_player_bid = ()
        pass
