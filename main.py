import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    def special_ability(self):
        pass

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def special_ability(self, opponent):
        self.attack_power = random.randint(1,50)
        opponent.health -= self.attack_power
        print(f'{self.name} used Warrior Smash on {opponent.name} for {self.attack_power}')
        
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)
    
    def attack(self, opponent):
        self.attack_power = random.randint(1,10)
        opponent.health -= self.attack_power
        print(f'{self.name} attacked {opponent.name} for {self.attack_power}')
    
    def special_ability(self, opponent):
        print('Please select a special ability!')
        print('----------------------------------')
        ability = int(input('1. Evade or 2. Quick Shot'))
        if ability == 1:
            opponent.attack = 0
            print(f'{self.name} evaded and took no damage from {opponent.name}')
        else:
            first_shot = random.randint(1, 10)
            second_shot = random.randint(1, 10)
            self.attack_power = first_shot + second_shot
            opponent.health -= self.attack_power
            print(f'{self.name} used quick shot! first arrow for {first_shot} and second arrow for {second_shot}!')
        
        
        


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
    
    def heal(self):
        if self.health <= 150:
            self.health += random.randint(1, 25)
        print(f'{self.name} healed themselves! Health at {self.health}')

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name)  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)  # Implement special abilities
        elif choice == '3':
            player.heal()  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()