#!/usr/bin/python3


from random import SystemRandom
from os import walk, system
from time import sleep

_sysrand = SystemRandom()


class Diceware(object):
    __dict = {}

    def __init__(self, numdice=None):
        self.len = 0
        self.passphrase = []
        self.wordlist = self.set_wordlist()
        self.read_wordlist()
        self.num_dice = len(list(self.__dict.keys())[0])

    def set_wordlist(self):
        wordlists = []
        for (_,_,files) in walk('.'):
            for f in [file for file in files if 'wordlist' in file]:
                wordlists.append(f)
            break

        print('Which word list to use?')
        for i, l in enumerate(sorted(wordlists)):
            print('{}: {}'.format(i+1, l))
        while True:
            try:
                resp = int(input())
                break
            except ValueError:
                print('Please enter an integer')
        return wordlists[resp-1]

    def read_wordlist(self):
        with open(self.wordlist, 'r') as f:
            for line in f:
                s = line.split()
                self.__dict[s[0]] = s[1]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return ' '.join(self.passphrase)

    def clean(self):
        self.passphrase = []

    def set_length(self):
        while True:
            try:
                self.len = int(input("How many words: "))
                break
            except ValueError:
                print("Oops!  That was not an integer.  Try again...")

    def build_word(self):
        exp, key = 1, 0
        for j in range(self.num_dice):  # builds the key digit by digit
            r = _sysrand._randbelow(6) + 1  # simulate a dice roll
            r *= exp  # *= (1, 10, 100, 1000, etc)
            key += r
            exp *= 10  # 1 -> 10 -> 100, etc
        return self.__dict[str(key)]

    def build_passphrase(self):
        self.set_length()
        for i in range(self.len):
            self.passphrase.append(self.build_word())


def main():
    d = Diceware()
    while True:
        d.clean()
        d.build_passphrase()
        print('\n{}\n'.format(d))
        again = input("Make another DiceWare passphrase? [y/N] : ")
        if again.lower() != 'y':
            system('clear')
            print('Goodbye')
            sleep(0.5)
            system('clear')
            d.clean()
            break


if __name__ == '__main__':
    main()
