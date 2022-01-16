import time
def decorator(func):
    def decor():
        print("*" * 39)
        func()
        print("*" * 39)
    return decor()
class NPC:
    def __init__(self, name):
        self.name = name
        self.backpack = []
        self.gold = 100

class Charecter(NPC):
    def __init__(self, name, gender, health=100):
        self.name = name
        self.gender = gender
        self.stats = [
            {"strange": 1},
            {"intelligent": 1},
            {"agility": 1},
        ]
        self.level = 1
        self.free_point = 0
        self.health = health
        self.exp = 0
        self.backpack = ["map", "Small health potion", "Large health potion", "Medium health potion"]
        self.quest_in_progress = [2]
        self.quest_finished = [5]
        self.x = 0
        self.y = 0

    def exercise(self):
        # self.exp += exp
        exp = 100
        if exp >= 100:
            self.level += 1
            self.free_point += 5
            print(f"Ваш уровень: {self.level}\n"
                  f"Ваш уровень повысился, пора прокачать навыки")
            for i in range(5):
                print(f"У вас {self.free_point} свободных очков, распределите их")
                stats = {1: "Сила", 2: "Интеллект", 3: "Ловкость", 4: "Пропустить"}
                for key, value in stats.items():
                    print(key, value)
                ch = input()
                if ch == "1":
                    self.stats[0]["strange"] += 1
                    self.free_point -= 1
                    print(f'Ваша сила: {self.stats[0]["strange"]}')
                elif ch == "2":
                    self.stats[1]["intelligent"] += 1
                    self.free_point -= 1
                    print(f'Ваша интеллект: {self.stats[1]["intelligent"]}')
                elif ch == "3":
                    self.stats[2]["agility"] += 1
                    self.free_point -= 1
                    print(f'Ваша ловкость: {self.stats[2]["agility"]}')
                




    # def move(self):
    #     with open('Перемещение.txt', 'r', encoding='utf-8') as file:
    #         ask = file.readline()
    #         ask2 = file.readline()
    #         ok_go = file.readline()
    #         r_way = file.readline()
    #         l_way = file.readline()
    #         u_way = file.readline()
    #         d_way = file.readline()
    #         s_way = file.readline()
    #         print(ask, ask2, sep="")
    #         go = input()
    #         command = go.lower()
    #         if command == "вправо":
    #             self.x += 1
    #             if self.x > 20:
    #                 print(s_way)
    #                 self.x -= 1
    #                 character.move()
    #             else:
    #                 print(ok_go, r_way, sep="")
    #                 character.move()
    #         elif command == "влево":
    #             self.x -= 1
    #             if self.x < 0:
    #                 print(s_way)
    #                 self.x += 1
    #                 character.move()
    #             else:
    #                 print(ok_go, l_way, sep="")
    #                 character.move()
    #         elif command == "вверх":
    #             self.y -= 1
    #             if self.y < 0:
    #                 print(s_way)
    #                 self.y += 1
    #                 character.move()
    #             else:
    #                 print(ok_go, u_way, sep="")
    #                 character.move()
    #         elif command == "вниз":
    #             self.y += 1
    #             if self.y > 8:
    #                 print(s_way)
    #                 self.y -= 1
    #                 character.move()
    #             else:
    #                 print(ok_go, d_way, sep='')
    #                 character.move()
    #         elif command == "другое":
    #             actions = {1: "Открыть карту", 2: "Открыть инвентарь", 3: "Открыть журнал заданий", 4: "Выход"}
    #             for key, value in actions.items():
    #                 print(key, value)
    #             action1 = input()
    #             if action1 == "1":

    def say(self):
        with open('Приветствие.txt', 'r', encoding='utf-8') as f:
            say = f.readlines()
            print(say)

    def attack(self):
        power_attack = self.stats[0]["strange"] + self.stats[2]["agility"] * 1.05
        return power_attack


class Animal:
    def __init__(self, name, level):
        self.name = name
        self.strange = int(level) * 2
        self.intelligent = int(level)
        self.level = level
        self.agility = int(level) * 0.5
        self.backpack = []
        self.health = int(level) * 20

    def attack(self):
        power_attack = int(self.strange) + int(self.agility) * 1.05
        return power_attack


character = Charecter('Nick', 'Мужской')
# npc1 = NPC('Кузнец')
Dog = Animal("Бешеный пес", 3)
Bear = Animal("Медведь", 5)
# character.move()
# character.say()
# print(character.attack())
character.exercise()
# character.attack()
# print(character.__dict__)
# print(npc1.__dict__)
# print(Dog.__dict__)

def open_the_map():
    if "map" in character.backpack:
        x = character.y
        y = character.x
        for i in range(8):
            for j in range(20):
                if j == y and i == x:
                    print("𓀛", end=' ')
                    continue
                elif j == 16 and i == 2:
                    print("C", end=' ')
                    continue
                elif j == 3 and i == 1:
                    print("V", end=' ')
                    continue
                elif j == 8 and i == 5:
                    print("W", end=' ')
                    continue
                elif j == 14 and i == 6:
                    print("L", end=' ')
                    continue
                elif j == 0 and i == 3:
                    print("R", end=' ')
                    continue
                elif j == 9 and i == 0:
                    print("T", end=' ')
                    continue
                print(".", end=' ')
            print()

def open_quest():
    print(f"Активные: {character.quest_in_progress}\n"
          f"Выполненные: {character.quest_finished}")

def open_backpack():
    print(character.backpack)

def move():
        with open('Перемещение.txt', 'r', encoding='utf-8') as file:
            ask = file.readline()
            ask2 = file.readline()
            ok_go = file.readline()
            r_way = file.readline()
            l_way = file.readline()
            u_way = file.readline()
            d_way = file.readline()
            s_way = file.readline()
            print(ask, ask2, sep="")
            go = input()
            command = go.lower()
            if command == "вправо":
                character.x += 1
                if character.x > 20:
                    print(s_way)
                    character.x -= 1
                    move()
                else:
                    print(ok_go, r_way, sep="")
                    move()
            elif command == "влево":
                character.x -= 1
                if character.x < 0:
                    print(s_way)
                    character.x += 1
                    move()
                else:
                    print(ok_go, l_way, sep="")
                    move()
            elif command == "вверх":
                character.y -= 1
                if character.y < 0:
                    print(s_way)
                    character.y += 1
                    move()
                else:
                    print(ok_go, u_way, sep="")
                    move()
            elif command == "вниз":
                character.y += 1
                if character.y > 8:
                    print(s_way)
                    character.y -= 1
                    move()
                else:
                    print(ok_go, d_way, sep='')
                    move()
            elif command == "другое":
                actions = {1: "Открыть карту", 2: "Открыть инвентарь", 3: "Открыть журнал заданий", 4: "Выход из игры"}
                for key, value in actions.items():
                    print(key, value)
                action1 = input()
                if action1 == "1":
                    open_the_map()
                    move()
                elif action1 == "2":
                    open_backpack()
                    move()
                elif action1 == "3":
                    open_quest()
                    move()
                elif action1 == "4":
                    print("Возвращайся скорее")
# move()

def small_heal():
    if "Small health potion" in character.backpack:
        if character.health >= 80:
            character.health = 100
            character.backpack.remove("Small health potion")
            print(f"Ваше здоровье: {round(character.health)}")
        else:
            character.health += 20
            character.backpack.remove("Small health potion")
            print(f"Ваше здоровье: {round(character.health)}")
    else:
        print("Такого зелья нет!")
def Medium_heal():
    if "Medium health potion" in character.backpack:
        if character.health >= 60:
            character.health = 100
            character.backpack.remove("Medium health potion")
            print(f"Ваше здоровье: {round(character.health)}")
        else:
            character.health += 40
            character.backpack.remove("Medium health potion")
            print(f"Ваше здоровье: {round(character.health)}")
    else:
        print("Такого зелья нет!")
def Large_heal():
    if "Large health potion" in character.backpack:
        if character.health >= 40:
            character.health = 100
            character.backpack.remove("Large health potion")
            print(f"Ваше здоровье: {round(character.health)}")
        else:
            character.health += 60
            character.backpack.remove("Large health potion")
            print(f"Ваше здоровье: {round(character.health)}")
    else:
        print("Такого зелья нет!")


def fight(enemy):
    if isinstance(enemy, Animal):
        while enemy.health > 0 and character.health >= 0:
            enemy.health = enemy.health - character.attack()
            character.health = character.health - enemy.attack()
            print(f"Ваше здоровье: {round(character.health)}\n"
                  f"Здоровье врага: {round(enemy.health)}")
            if character.health < 30:
                if character.health <= 0:
                    print("Вы проиграли")
                    break
                else:
                    actions = {1: "Выпить зелье", 2: "Бежать", 3: "Продолжить"}
                    print(actions)
                    action = input()
                if action == "1":
                    choice = {1: "Малое", 2: "Среднее", 3: "Большое"}
                    print(choice)
                    ch = input()
                    if ch == "1":
                        small_heal()
                    elif ch == "2":
                        Medium_heal()
                    elif ch == "3":
                        Large_heal()
                elif action == "2":
                    move()
                elif action == "3":
                    continue
            time.sleep(0.3)
        if enemy.health <= 0:
            print("Вы победили")
            character.exercise(int(enemy.level) * 10)
            character.backpack.extend(enemy.backpack)
            move()
# fight(Bear)


