from project.player import Player


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(str(player.name))

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type != "Food" and sustenance_type != "Drink":
            return
        idx, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + supply.energy, Player.DEFAULT_STAMINA)
        self.supplies.pop(idx)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = ''
        if first_player.stamina == 0:
            result += f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina == 0:
            result += "\n" + f"Player {second_player.name} does not have enough stamina."
        if result:
            return result.strip()

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_win = self.__attack(first_player, second_player)
        if first_player_win:
            return f"Winner: {first_player.name}"

        second_player_win = self.__attack(second_player, first_player)
        if second_player_win:
            return f"Winner: {second_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return '\n'.join([str(p) for p in self.players]) + \
               '\n' + '\n'.join([s.details() for s in self.supplies])

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, 0, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return idx, supply
        return -1, None

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __attack(self, attacker, enemy):
        attacker.damage = attacker.stamina / 2
        enemy.stamina = max(enemy.stamina - attacker.damage, 0)
        return enemy.stamina == 0
