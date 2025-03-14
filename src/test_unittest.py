import unittest
from argparse import Namespace
from encounter_builder import generate_encounter

class TestMain(unittest.TestCase):
    def test_generate_encounter_normal(self):
        # set the expected dict
        expected = {'Pixie': {'Type': 'Fey', 'ChallengeRating': '1/4', 'Environment': ['Forest'], 'Plane': ['Feywild'], 'Book': 'Monster Manual 2024', 'Page': '244', 'Amount': 2}, 'Stirge': {'Type': 'Monstrosity', 'ChallengeRating': '1/8', 'Environment': ['Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '299', 'Amount': 2}, 'Awakened Shrub': {'Type': 'Plant', 'ChallengeRating': '0', 'Environment': ['Forest'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '23', 'Amount': 3}, 'Homunculus': {'Type': 'Construct', 'ChallengeRating': '0', 'Environment': ['Artic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Underwater', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '172', 'Amount': 4}, 'Bandit': {'Type': 'Humanoid', 'ChallengeRating': '1/8', 'Environment': ['Artic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Underwater', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '27', 'Amount': 1}, 'Swarm of Rats ': {'Type': 'Beast', 'ChallengeRating': '1/4', 'Environment': ['Forest', 'Swamp', 'Underdark', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '370', 'Amount': 1}}

        # set the args, without having to input any into the test yourself
        args = Namespace(environment=None, level=1, size=4, plane=None, type=None, difficulty='Moderate', min_exp=None, max_creatures=None)

        # generate an encounter using a seed
        encounter = generate_encounter(args, seed=45)

        #test if it outputs the correct value
        self.assertEqual(expected, encounter)

    def test_generate_encounter_size_level(self):
        # set the expected dict
        expected = {'Satyr Revelmaster': {'Type': 'Fey', 'ChallengeRating': '6', 'Environment': ['Forest'], 'Plane': ['Feywild'], 'Book': 'Monster Manual 2024', 'Page': '268', 'Amount': 1}, 'Bandit': {'Type': 'Humanoid', 'ChallengeRating': '1/8', 'Environment': ['Artic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Underwater', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '27', 'Amount': 1}, 'Ankheg': {'Type': 'Monstrosity', 'ChallengeRating': '2', 'Environment': ['Forest', 'Grassland'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '18', 'Amount': 1}, 'Water Weird': {'Type': 'Elemental', 'ChallengeRating': '3', 'Environment': ['Underdark', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '323', 'Amount': 1}, 'Swarm of Rats ': {'Type': 'Beast', 'ChallengeRating': '1/4', 'Environment': ['Forest', 'Swamp', 'Underdark', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '370', 'Amount': 2}, 'Pixie': {'Type': 'Fey', 'ChallengeRating': '1/4', 'Environment': ['Forest'], 'Plane': ['Feywild'], 'Book': 'Monster Manual 2024', 'Page': '244', 'Amount': 1}, 'Stirge': {'Type': 'Monstrosity', 'ChallengeRating': '1/8', 'Environment': ['Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '299', 'Amount': 1}, 'Homunculus': {'Type': 'Construct', 'ChallengeRating': '0', 'Environment': ['Artic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Underwater', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '172', 'Amount': 4}, 'Zombie': {'Type': 'Undead', 'ChallengeRating': '1/4', 'Environment': ['Underdark', 'Urban'], 'Plane': ['Shadowfell'], 'Book': 'Monster Manual 2024', 'Page': '308', 'Amount': 1}, 'Awakened Shrub': {'Type': 'Plant', 'ChallengeRating': '0', 'Environment': ['Forest'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '23', 'Amount': 1}}

        # set the args, without having to input any into the test yourself
        args = Namespace(environment=None, level=5, size=5, plane=None, type=None, difficulty='Moderate', min_exp=None, max_creatures=None)

        # generate an encounter using a seed
        encounter = generate_encounter(args, seed=45)

        #test if it outputs the correct value
        self.assertEqual(expected, encounter)

    def test_generate_encounter_size_level_env(self):
        # set the expected dict
        expected = {'Pixie': {'Type': 'Fey', 'ChallengeRating': '1/4', 'Environment': ['Forest'], 'Plane': ['Feywild'], 'Book': 'Monster Manual 2024', 'Page': '244', 'Amount': 1}, 'Oni': {'Type': 'Fiend', 'ChallengeRating': '7', 'Environment': ['Forest', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '232', 'Amount': 1}, 'Awakened Shrub': {'Type': 'Plant', 'ChallengeRating': '0', 'Environment': ['Forest'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '23', 'Amount': 2}, 'Bandit': {'Type': 'Humanoid', 'ChallengeRating': '1/8', 'Environment': ['Artic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Underwater', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '27', 'Amount': 2}, 'Swarm of Rats ': {'Type': 'Beast', 'ChallengeRating': '1/4', 'Environment': ['Forest', 'Swamp', 'Underdark', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '370', 'Amount': 1}, 'Ankheg': {'Type': 'Monstrosity', 'ChallengeRating': '2', 'Environment': ['Forest', 'Grassland'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '18', 'Amount': 1}, 'Dire Wolf': {'Type': 'Beast', 'ChallengeRating': '1', 'Environment': ['Forest', 'Hill'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '352', 'Amount': 1}, 'Homunculus': {'Type': 'Construct', 'ChallengeRating': '0', 'Environment': ['Artic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Swamp', 'Underdark', 'Underwater', 'Urban'], 'Plane': [], 'Book': 'Monster Manual 2024', 'Page': '172', 'Amount': 3}}

        # set the args, without having to input any into the test yourself
        args = Namespace(environment=["forest"], level=5, size=5, plane=None, type=None, difficulty='Moderate', min_exp=None, max_creatures=None)

        # generate an encounter using a seed
        encounter = generate_encounter(args, seed=45)

        #test if it outputs the correct value
        self.assertEqual(expected, encounter)

    def test_generate_encounter_size_level_creature_limit(self):
        # set the expected dict
        expected = {'Satyr Revelmaster': {'Type': 'Fey', 'ChallengeRating': '6', 'Environment': ['Forest'], 'Plane': ['Feywild'], 'Book': 'Monster Manual 2024', 'Page': '268', 'Amount': 1}}

        # set the args, without having to input any into the test yourself
        args = Namespace(environment=None, level=5, size=5, plane=None, type=None, difficulty='Moderate', min_exp=None, max_creatures=1)

        # generate an encounter using a seed
        encounter = generate_encounter(args, seed=45)

        #test if it outputs the correct value
        self.assertEqual(expected, encounter)

    def test_generate_encounter_size_level_boss(self):
        # set the expected dict
        expected = {'Leviathan': {'Type': 'Elemental', 'ChallengeRating': '20', 'Environment': ['Underwater', 'Coastal'], 'Plane': [], 'Book': "Mordenkainen's Tome of Foes", 'Page': '198', 'Amount': 1}}

        # set the args, without having to input any into the test yourself
        args = Namespace(environment=None, level=15, size=5, plane=None, type=None, difficulty='High', min_exp=23500, max_creatures=1)

        # generate an encounter using a seed
        encounter = generate_encounter(args, seed=45)

        #test if it outputs the correct value
        self.assertEqual(expected, encounter)

    if __name__ == "__main__":
        unittest.main()