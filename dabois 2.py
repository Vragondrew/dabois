import random
import time

class Fighter:
    def __init__(self, name, attacks):
        self.name = name
        if self.name == "Rihaan":
            self.max_hp = 230 # Rihaan has 30 more HP
        else:
            self.max_hp = 200
        self.hp = self.max_hp
        self.attacks = attacks

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_opponent(self, opponent, attack_idx):
        attack_name, attack_power, hit_chance, critical_chance = self.attacks[attack_idx]
          

         # Check if the attacker is Rihaan and the attack is "Parent Summoning"
        if self.name == "Rihaan" and attack_name == "Parent Summoning":
            summon = random.choice(["Mom", "Dad"])
            if summon == "Mom":
                self.hp = max(1, self.hp // 2)  # Reduce HP by half
                print("Rihaan summons Mom! His HP is reduced by half!")
            else:
                attack_power *= 2  # Double the attack power
                print("Rihaan summons Dad! His next attack will be greatly empowered!")
                # Apply the attack boost for the next attack
                
         # Check if the attacker is Hari and the attack is "Mind Manipulation"
        if self.name == "Hari" and attack_name == "Mind Manipulation":
            if opponent.name == "Ragav":
                for opp_attack in opponent.attacks:
                    if opp_attack[0] == "Sigma Mindset":
                        print("Hari's Mind Manipulation fails against Ragav's Sigma Mindset!")
                        return  # Exit the method without performing the attack

          # Check if the attacker is Venkat and the attack is "Penis Lasso"
        if self.name == "Venkat" and attack_name == "Penis Lasso":
            if opponent.name == "Rihaan":
                attack_power *= 1.5  # Increase the attack power by 50% against Rihaan
                print("Venkat's Penis Lasso deals extra damage to Rihaan!")
            elif opponent.name == "Yusuf":
                attack_power *= 0.75  # Reduce the attack power by 25% against Yusuf
                print("Venkat's Penis Lasso deals less damage to Yusuf!")
        
        # Check if both fighters are using their respective special attacks
        if self.name == "Hari" and opponent.name == "Venkat" and \
            attack_name == "Dirty Deeds Done Jerk Off" and \
            any(attack[0] == "Dio Rampage" for attack in opponent.attacks):
            print("Venkat: MUDA MUDA MUDA MUDA")
            print("Hari: ORA ORA ORA ORA")

             # Check if the attacker is Hari and the attack is "Trash Talk"
        if self.name == "Hari" and attack_name == "Trash Talk":
            # Find Ragav's "Depression" attack and increase its attack power
            for idx, (name, power, _, _) in enumerate(opponent.attacks):
                if name == "Depression":
                    opponent.attacks[idx] = (name, power + 10, _, _)
                    print("Hari's Trash Talk empowers Ragav's Depression!")
                    break

             # Check if Rihaan is the opponent and the attack is "Buddysta Brawl"
        if self.name == "Rihaan" and attack_name == "Buddysta Brawl" and not self.dog_eaten:
            if random.random() <= 0.25:  # 25% chance of eating the dog
                self.dog_eaten = True
                print("Rihaan eats your dog! Buddysta Brawl can never be used again!")
            else:
                print("Rihaan dodges the attack!")
        
        # Rest of the attack logic remains the same
        if random.random() <= hit_chance:  # Check if the fighter lands the attack
            damage = random.randint(attack_power - 5, attack_power + 5)
            if random.random() <= critical_chance:  # Check if the attack is critical
                damage *= 2  # Double the damage for critical attacks
                critical_comments = ["DEVASTATING!", "INCREDIBLE!", "UNSTOPPABLE!"]
                critical_comment = random.choice(critical_comments)
                print(f"{self.name} strikes with {attack_name}! {critical_comment} It's a critical hit, inflicting {damage} damage to {opponent.name}!")
            else:
                hit_comments = ["with full force!", "with precision!", "with accuracy!"]
                hit_comment = random.choice(hit_comments)
                print(f"{self.name} executes {attack_name} {hit_comment} It deals {damage} damage to {opponent.name}!")
            opponent.take_damage(damage)
        else:
            miss_comments = ["but misses completely!", "but the attack goes wide!", "but it fails to connect!"]
            miss_comment = random.choice(miss_comments)
            print(f"{self.name} attempts {attack_name} {miss_comment}")

    def is_alive(self):
        return self.hp > 0

class Trainer:
    def __init__(self, name):
        self.name = name
        self.fighter = None

    def choose_fighter(self, available_fighters):
        print(f"{self.name}, choose your fighter:")
        for i, fighter in enumerate(available_fighters, 1):
            print(f"{i}. {fighter.name}")
        choice = int(input("Enter your choice: ")) - 1
        self.fighter = available_fighters.pop(choice)

    def choose_attack(self):
        print(f"{self.name}, choose a move for {self.fighter.name} to execute:")
        for i, (attack_name, _, _, _) in enumerate(self.fighter.attacks, 1):
            print(f"{i}. {attack_name}")
        return int(input("Enter your choice: ")) - 1

def print_health_bar(name, current_hp, max_hp):
    bar_length = 20
    filled_bar = int((current_hp / max_hp) * bar_length)
    empty_bar = bar_length - filled_bar
    health_bar = "[" + "#" * filled_bar + "-" * empty_bar + "]"
    print(f"{name}'s health: {current_hp}/{max_hp} {health_bar}")

def battle(player1, player2):
    print("\nLet the battle begin!\n")
    while player1.fighter.is_alive() and player2.fighter.is_alive():
        p1_attack_idx = player1.choose_attack()
        p2_attack_idx = player2.choose_attack()

        player1.fighter.attack_opponent(player2.fighter, p1_attack_idx)
        player2.fighter.attack_opponent(player1.fighter, p2_attack_idx)
        
        print_health_bar(player1.fighter.name, player1.fighter.hp, player1.fighter.max_hp)
        print_health_bar(player2.fighter.name, player2.fighter.hp, player2.fighter.max_hp)
        print()

        time.sleep(1)  # Add a delay for better visualization

    if player1.fighter.is_alive():
        print(f"{player1.name} emerges victorious! A display of unmatched strength and skill!")
    elif player2.fighter.is_alive():
        print(f"{player2.name} proves victorious! A remarkable feat of perseverance and power!")
    else:
        print("The battle ends in a draw! Both fighters have reached their limits!")

def main():
    while True:
        fighters = [
            Fighter("Rihaan", [("Judgement", random.randint(15, 25), 0.8, 0.1), 
                       ("Gyat", random.randint(12, 20), 0.7, 0.15), 
                       ("Break Dance!", random.randint(18, 28), 0.75, 0.2),
                       ("Parent Summoning", random.randint(20, 30), 0.7, 0.1)]),
            
            Fighter("Hari", [("Dirty Deeds Done Jerk Off", random.randint(25, 35), 0.75, 0.1), 
                             ("Killer Curd", random.randint(22, 30), 0.85, 0.2), 
                             ("Trash Talk", random.randint(25, 35), 0.8, 0.1),
                             ("Mind Manipulation", random.randint(20, 30), 0.75, 0.15)]),
            
            Fighter("Ragav", [("Basketball Cannon", random.randint(30, 40), 0.7, 0.1), 
                              ("Depression", random.randint(28, 35), 0.8, 0.15), 
                              ("Sigma Mindset", random.randint(30, 40), 0.7, 0.15),
                              ("Kfc Chicken", random.randint(25, 35), 0.75, 0.1)]),
            
            Fighter("Yusuf", [("Bomb Blast", random.randint(25, 35), 0.85, 0.1), 
                              ("Testicle Bite", random.randint(23, 30), 0.85, 0.2), 
                              ("Shoulder Strike", random.randint(23, 30), 0.85, 0.2),
                              ("9/11", random.randint(20, 30), 0.85, 0.15)]),
            
            Fighter("Venkat", [("Penis Lasso", random.randint(30, 40), 0.75, 0.1),
                      ("Buddysta Brawl", random.randint(27, 35), 0.85, 0.15), 
                      ("Gang Signs", random.randint(33, 40), 0.8, 0.2),
                      ("Dio Rampage", random.randint(30, 40), 0.8, 0.1)]),]

        random.shuffle(fighters)

        player1_name = input("Enter a name that is not your real name (Player 1): ")
        player1 = Trainer(player1_name)
        player1.choose_fighter(fighters)

        player2_name = input("Enter a name that is not your real name (Player 2): ")
        player2 = Trainer(player2_name)
        player2.choose_fighter(fighters)

        battle(player1, player2)
        print("PC: MUHAKAHAHA")
        if player1.fighter.is_alive():
            print(f"PC: {player1.name} stands triumphant, showcasing unparalleled strength and strategy!")
        elif player2.fighter.is_alive():
            print(f"PC: {player2.name} emerges victorious, a testament to their unwavering determination and prowess!")
        else:
            print("PC: The battle concludes in a draw, both fighters displaying remarkable skill and tenacity!")
        
        end_game = input("Press '1' to end the game or any other key to play again: ")
        if end_game == "1":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
