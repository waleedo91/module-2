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
    
    def heal(self):
        if self.health <= 120:
            self.health += 5
            print(f'{self.name} healed for 5 health points!')
            print(f'{self.name} has {self.health} left')
        else:
            print(f'{self.name} is already at max health!')

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    def attack(self, opponent):
        self.attack_power = random.randint(1,40)
        opponent.health -= self.attack_power
        print(f'{self.name} attacked {opponent.name} for {self.attack_power}!')    
    
    def special_ability(self, opponent):
        self.attack_power = random.randint(1,50)
        opponent.health -= self.attack_power
        print(f'{self.name} used Warrior Smash on {opponent.name} for {self.attack_power}')
        
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def attack(self, opponent):
        self.attack_power = random.randint(1,15)
        opponent.health -= self.attack_power
        print(f'{self.name} attacked {opponent.name} for {self.attack_power}!')

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
        print('1. Evade')
        print('2. Quick Shot')
        ability = int(input('Please select an ability! '))
        if ability == 1:
            self.health += 15
            print(f'{self.name} evaded and took no damage from {opponent.name}')
            
        if ability == 2:
            first_shot = random.randint(1, 20)
            second_shot = random.randint(1, 20)
            self.attack_power = first_shot + second_shot
            opponent.health -= self.attack_power
            print(f'{self.name} used quick shot! first arrow for {first_shot} and second arrow for {second_shot}!')
            
    
        

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
        
    def attack(self, opponent):
        self.attack_power = random.randint(1,30)
        print(f'{self.name} attacked the {opponent.name} for {self.attack_power}!')
    
    def special_ability(self, opponent):
        print('Please select a special ability!')
        print('----------------------------------')
        print('1. Holy Strike')
        print('2. Divine Shield')
        ability = int(input('Please select an ability! '))
        
        if ability == 1:
            chance = random.randint(1,10)
            if chance >= 5:
                self.attack_power += 20
                print(f'{self.name} used Holy strike against {opponent.name} for {self.attack_power}')
            
        if ability == 2:
            self.health += 15
            print(f'{self.name} used Divine Shield and took no damage!')     

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