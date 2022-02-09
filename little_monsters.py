class Player:
    player_id = 0
    def __init__(self, input_name, input_team):
        Player.player_id += 1
        self.id = Player.player_id
        self.name = input_name
        self.team = input_team
    
    def __repr__(self, self.name, self.team, self.id):
        print("Player " + str(self.id) + "'s name is " + self.name + " and they have the following monsters in their team: " + self.team)


player_one = Player()