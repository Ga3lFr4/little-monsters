class Player:
    player_id = 0
    def __init__(self, input_name, input_team):
        Player.player_id += 1
        self.id = Player.player_id
        self.name = input_name
        self.team = input_team
        self.active_monster = None
        self.money = 100
        self.ko_monsters = None
    
    def __repr__(self):
        repr_string = "Player " + str(self.id) + "'s name is " + self.name + " and they have the following monsters in their team: "
        for monster in self.team:
            if monster == self.team[-1]:
                repr_string = repr_string + monster + "."
            else:
                repr_string = repr_string + monster + ", "
        return repr_string

class Monster:
    weaknesses = {'Fire' : 'Water', 'Water' : 'Plant', 'Plant' : 'Fire'}

    def __init__(self, name, type, level = 5):
        self.name = name
        self.type = type
        self.level = level
        self.hp = int(self.level * 10)
        self.is_ko = False
        self.is_affected = False
        self.is_active = False
        self.weakness = Monster.weaknesses[self.type]
    
    def __repr__(self):
        return self.name + ' is a ' + self.type + ' monster and is currently level ' + str(self.level) + ', its weakness is : ' + self.weakness

a = ('Charmander', 'Fire')
b = ('Squirtle', 'Water')
c = ('Bulbasaur', 'Plant')

#player_one = Player('Gaël', ['Charmander', 'Bulbasaur'])
#player_two = Player('Théo', ['Squirtle', 'Buterfree'])
#print(player_two)

charmander = Monster('Charmander', 'Fire')
print(charmander)