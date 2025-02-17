import random

low_complexity_spirits = ["River Surges in Sunlight", "Shadows Flicker like Flame", "Vital Strength of the Earth",
                          "Lightning's Swift Strike"]

moderate_complexity_spirits = ["Keeper of the Forbidden Wilds", "Volcano Looming High", "Many Minds Move as One",
                               "Sharp Fangs Behind the Leaves", "A Spread of Rampant Green", "Thunderspeaker",
                               "Grinning Trickster Stirs Up Trouble", "Lure of the Deep Wilderness",
                               "Shifting Memory of Ages", "Stone's Unyielding Defiance"]

high_complexity_spirits = ["Bringer of Dreams and Nightmares", "Ocean's Hungry Grasp", "Heart of the Wildfire",
                           "Serpent Slumbering Beneath the Island", "Shroud of Silent Mist",
                           "Vengeance as a Burning Plague", "Downpour Drenches the World"]

very_high_complexity_spirits = ["Fractured Days Split the Sky", "Starlight Seeks Its Form", "Finder of Paths Unseen"]

low_to_moderate_complexity_spirits = (low_complexity_spirits + moderate_complexity_spirits)
low_to_high_complexity_spirits = (low_to_moderate_complexity_spirits + high_complexity_spirits)
all_spirits = (low_to_high_complexity_spirits + very_high_complexity_spirits)

class Adversary:
    def __init__(self, name, difficulty_list):
        self.name = name
        self.difficulty_list = difficulty_list

    def return_name(self):
        return self.name

    def return_difficulty(self, level):
        return self.difficulty_list[level]

class Scenario:
    def __init__(self, name, min_difficulty, max_difficulty):
        self.name = name
        self.min_difficulty = min_difficulty
        self.max_difficulty = max_difficulty

    def return_name(self):
        return self.name

    def return_min_difficulty(self):
        return self.min_difficulty

    def return_max_difficulty(self):
        return self.max_difficulty

adversaries = [Adversary("Brandenburg-Prussia", [1, 2, 4, 6, 7, 9, 10]), Adversary("England", [1, 3, 4, 6, 7, 9, 11]),
               Adversary("Sweden", [1, 2, 3, 5, 6, 7, 8]),
               Adversary("France (Plantation Colony)", [2, 3, 5, 7, 8, 9, 10]),
               Adversary("Scotland", [1, 3, 4, 6, 7, 8, 10]), Adversary("Russia", [1, 3, 4, 6, 7, 9, 11]),
               Adversary("Habsburg Monarchy (Livestock Colony)", [2, 3, 5, 6, 8, 9, 10])]

scenarios = [Scenario("Blitz", 0, 0), Scenario("Guard the Isle's Heart", 0, 0), Scenario("Rituals of Terror", 3, 3),
             Scenario("Dahan Insurrection", 4, 4), Scenario("Second Wave", -1, 1),
             Scenario("Powers Long Forgotten", 0, 1), Scenario("Ward the Shores", 2, 2),
             Scenario("Rituals of the Destroying Flame", 3, 3), Scenario("Elemental Invocation", -1, 3),
             Scenario("Despicable Theft", 2, 2), Scenario("The Great River", 3, 3),
             Scenario("A Diversity of Spirits", 0, 0), Scenario("Varied Terrains", 2, 2)]



def validate_spirit_complexity(complexity):
    if (complexity == "low" or complexity == "l" or complexity == "moderate" or complexity == "m"
            or complexity == "high" or complexity == "h" or complexity == "very high" or complexity == "v"):
        return True
    else:
        return False

def validate_adversary_or_combined_difficulty(difficulty):
    try:
        if int(difficulty) >= 1:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_scenario_difficulty(difficulty):
    try:
        if int(difficulty) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def randomize_spirit(complexity_cap):
    if complexity_cap == "low" or complexity_cap == "l":
        random_int = random.randint(0, len(low_complexity_spirits) - 1)
        return low_complexity_spirits[random_int]
    elif complexity_cap == "moderate" or complexity_cap == "m":
        random_int = random.randint(0, len(low_to_moderate_complexity_spirits) - 1)
        return low_to_moderate_complexity_spirits[random_int]
    elif complexity_cap == "high" or complexity_cap == "h":
        random_int = random.randint(0, len(low_to_high_complexity_spirits) - 1)
        return low_to_high_complexity_spirits[random_int]
    else:
        random_int = random.randint(0, len(all_spirits) - 1)
        return all_spirits[random_int]

def randomize_adversary(cap):
    adversary = adversaries[random.randint(0, len(adversaries) - 1)]
    # if even the base difficulty of the randomized adversary is higher than the cap, a reroll of adversary is needed
    # (happens only for Hasburg or France, base difficulty of 2)
    while adversary.return_difficulty(0) > cap:
        adversary = adversaries[random.randint(0, len(adversaries) - 1)]
    level = random.randint(0, 6)
    while adversary.return_difficulty(level) > cap:
        level = random.randint(0, 6)
    return adversary.return_name(), level, adversary.return_difficulty(level)

def randomize_scenario(cap):
    scenario = scenarios[random.randint(0, len(scenarios) - 1)]
    while scenario.return_max_difficulty() > cap:
        scenario = scenarios[random.randint(0, len(scenarios) - 1)]
    return scenario.return_name(), scenario.return_min_difficulty(), scenario.return_max_difficulty()

def main():
    print("Welcome to the Spirit Island randomizer")
    answer = input("Select the thing you would like to have picked ((s)pirit, (a)dversary, (sc)enario, all) "
                   "or end randomizing (end): ")
    while answer != "end":
        if answer == "spirit" or answer == "s":
            complexity_cap = input("Maximum allowed spirit complexity ((l)ow, (m)oderate, (h)igh, (v)ery high): ")
            if validate_spirit_complexity(complexity_cap):
                print(randomize_spirit(complexity_cap))
            else:
                print("Invalid complexity")
        elif answer == "adversary" or answer == "a":
            difficulty_cap = input("Maximum allowed adversary difficulty (from 1 to 11): ")
            if validate_adversary_or_combined_difficulty(difficulty_cap):
                adversary_name, adversary_level, adversary_difficulty = randomize_adversary(int(difficulty_cap))
                print("{} level {}, difficulty {}".format(adversary_name, adversary_level, adversary_difficulty))
            else:
                print("Invalid difficulty")
        elif answer == "scenario" or answer == "sc":
            difficulty_cap = input("Maximum allowed scenario difficulty (from 0 to 4): ")
            if validate_scenario_difficulty(difficulty_cap):
                scenario_name, scenario_min_difficulty, scenario_max_difficulty\
                    = randomize_scenario(int(difficulty_cap))
                if scenario_min_difficulty != scenario_max_difficulty:
                    print("{}, difficulty ranging from {} to {}"
                          .format(scenario_name, scenario_min_difficulty, scenario_max_difficulty))
                else:
                    print("{}, difficulty {}".format(scenario_name, scenario_max_difficulty))
            else:
                print("Invalid difficulty")
        elif answer == "all":
            complexity_cap = input("Maximum allowed complexity for your spirit"
                                   " ((l)ow, (m)oderate, (h)igh, (v)ery high): ")
            difficulty_cap = input("Maximum allowed combined adversary and scenario difficulty (from 1 to 15): ")
            if validate_spirit_complexity(complexity_cap):
                print(randomize_spirit(complexity_cap))
            else:
                print("Invalid complexity")
            if validate_adversary_or_combined_difficulty(difficulty_cap):
                adversary_name, adversary_level, adversary_difficulty = randomize_adversary(int(difficulty_cap))
                scenario_name, scenario_min_difficulty, scenario_max_difficulty \
                    = randomize_scenario(int(difficulty_cap))
                while adversary_difficulty + scenario_max_difficulty > int(difficulty_cap):
                    adversary_name, adversary_level, adversary_difficulty = randomize_adversary(int(difficulty_cap))
                    scenario_name, scenario_min_difficulty, scenario_max_difficulty \
                        = randomize_scenario(int(difficulty_cap))
                print("{} level {}, difficulty {}".format(adversary_name, adversary_level, adversary_difficulty))
                if scenario_min_difficulty != scenario_max_difficulty:
                    print("{}, difficulty ranging from {} to {}"
                          .format(scenario_name, scenario_min_difficulty, scenario_max_difficulty))
                else:
                    print("{}, difficulty {}".format(scenario_name, scenario_max_difficulty))
                if scenario_min_difficulty != scenario_max_difficulty:
                    print("Combined difficulty ranging from {} to {}"
                          .format(adversary_difficulty + scenario_min_difficulty,
                                  adversary_difficulty + scenario_max_difficulty))
                else:
                    print("Combined difficulty {}".format(adversary_difficulty + scenario_max_difficulty))
            else:
                print("Invalid difficulty")


        else:
            print("Invalid command")

        print()
        answer = input("Randomize more ((s)pirit, (a)dversary, (sc)enario, all) or end randomizing (end): ")

    print()
    print("Good luck, have fun!")

if __name__=="__main__":
    main()