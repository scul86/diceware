#!/usr/bin/python3


from random import randint, seed
from os import urandom


class Diceware:
    __dict = {}

    def __init__(self):
        self.passphrase = []
        with open('dicewarewordlist.txt', 'r') as f:
            for line in f:
                s = line.split()
                self.__dict[s[0]] = s[1]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return ' '.join(self.passphrase)

    def build_passphrase(self, l):
        for i in range(l):
            e, key = 1, 0
            seed(urandom(16))
            for j in range(5): # builds the key digit by digit
                r = randint(1, 6) # simulate a dice roll
                r *= e # *= (1, 10, 100, 1000, etc)
                key += r
                e *= 10 # 1 -> 10 -> 100, etc
            self.passphrase.append(self.__dict[str(key)])
        val = None


def main():
    while True:
        try:
            num = int(input("How many words: "))
            break
        except ValueError:
            print("Oops!  That was not an integer.  Try again...")
    d = Diceware()
    d.build_passphrase(num)
    print(d)

if __name__ == '__main__':
    main()
