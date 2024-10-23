import random


class Weapon:
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        damage = random.randint(10, 20)
        return damage, f"наносит рубящий удар мечом на {damage} урона"


class Bow(Weapon):
    def attack(self):
        damage = random.randint(8, 25)
        return damage, f"выпускает стрелу из лука на {damage} урона"


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def get_status(self):
        return f"{self.name} (HP: {self.health}/{self.max_health})"


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} берёт в руки новое оружие")

    def attack_monster(self, monster):
        if self.weapon is None:
            print(f"{self.name} не может атаковать без оружия!")
            return

        damage, attack_description = self.weapon.attack()
        print(f"{self.name} {attack_description}")

        monster.take_damage(damage)
        print(f"Состояние монстра: {monster.get_status()}")


def main():
    fighter = Fighter("Герой")
    monster = Monster("Гоблин", 50)

    print("\n=== Начало боя ===")
    print(f"Появился {monster.get_status()}")

    fighter.change_weapon(Sword())
    while monster.is_alive():
        fighter.attack_monster(monster)
        if not monster.is_alive():
            print(f"{monster.name} побеждён!")

    monster = Monster("Орк", 60)
    print(f"\nПоявился новый противник: {monster.get_status()}")

    fighter.change_weapon(Bow())
    while monster.is_alive():
        fighter.attack_monster(monster)
        if not monster.is_alive():
            print(f"{monster.name} побеждён!")


if __name__ == "__main__":
    main()