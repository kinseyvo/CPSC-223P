from random import randint

class Die:
    """A class to model a Die"""

    def __init__(self, sides=6):
        """Initialziation class with one attribute"""
        self.sides = sides

    def roll_die(self):
        """Using randit to get a number between the number 1 and the number of sides the die has"""
        print(randint(1, self.sides))


die_1 = Die()
print("Rolling Die #1 10 times:")
for i in range(1,11):
    die_1.roll_die()

die_2 = Die(10)
print("\nRolling Die #2 10 times:")
for i in range(1,11):
    die_2.roll_die()

die_3 = Die(20)
print("\nRolling Die #3 10 times:")
for i in range(1,11):
    die_3.roll_die()