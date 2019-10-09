#!/usr/bin/env python


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # calculate the bulls
        bull = 0

        new_secret = []
        new_guess = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                new_secret.append('/')
                new_guess.append('*')
            else:
                new_secret.append(secret[i])
                new_guess.append(guess[i])

        guess = ''.join(new_guess)
        secret = ''.join(new_secret)

        # calculate the cows
        cow = 0

        for i in range(len(secret)):
            shouldAdd = False
            for j in range(len(guess)):
                if secret[i] == guess[j]:
                    shouldAdd = True
                    if i == j:
                        # Totally ruined
                        shouldAdd = False
                        break
            if shouldAdd:
                cow += 1

        return "%dA%dB" % (bull, cow)
