import random


class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10, 36) if i % 2 == 0]
        self.dumbbell_holder = {}
        self.restar()

    def restar(self):
        self.dumbbell_holder = {i: i for i in self.dumbbells}

    def list_dumbbells(self):
        return [i for i in self.dumbbell_holder.values() if i != 0]

    def list_slots(self):
        return [i for i, j in self.dumbbell_holder.items() if j == 0]

    def pick_dumbbell(self, peso):
        halt_pos = list(self.dumbbell_holder.values()).index(peso)
        key_halt = list(self.dumbbell_holder.keys())[halt_pos]
        self.dumbbell_holder[key_halt] = 0
        return peso

    def place_dumbbell(self, pos, peso):
        self.dumbbell_holder[pos] = peso

    def calculate_caos(self):
        num_caos = [i for i, j in self.dumbbell_holder.items() if i != j]
        return len(num_caos) / len(self.dumbbell_holder)


class User:
    def __init__(self, user_type, gym):
        self.user_type = user_type
        self.gym = gym
        self.weight = 0

    def start_training(self):
        lista_pesos = self.gym.list_dumbbells()
        self.weight = random.choice(lista_pesos)
        self.gym.pick_dumbbell(self.weight)

    def end_training(self):
        espacos = self.gym.list_slots()

        if self.user_type == 1:
            if self.weight in espacos:
                self.gym.place_dumbbell(self.weight, self.weight)
            else:
                pos = random.choice(espacos)
                self.gym.place_dumbbell(pos, self.weight)

        if self.user_type == 2:
            pos = random.choice(espacos)
            self.gym.place_dumbbell(pos, self.weight)
        self.weight = 0


gym = Gym()

users = [User(1, gym) for i in range(10)]
users += [User(2, gym) for i in range(1)]
random.shuffle(users)

for i in range(10):
    random.shuffle(users)
    for user in users:
        user.start_training()
    for user in users:
        user.end_training()

print(gym.dumbbell_holder)
print(gym.calculate_caos())
