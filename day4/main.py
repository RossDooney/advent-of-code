import os
import re





def main():
    part1()
    part2()


def part1():
    f = open("input.txt", "r")
    total = 0
    for line in f:
        subTotal = 0
        winngNumbers, playerNumbers = parseLine(line)
        for playerNumber in playerNumbers.split():
            if playerNumber in winngNumbers.split():
                if subTotal == 0:
                    subTotal += 1
                else:
                    subTotal *= 2

        total += subTotal
    print("Part 1: ", total)
    f.close()
            

def part2():
    f = open("input.txt", "r")
    total = 0
    card_index= [0]

    for line in f:
        i = 0
        try:
            card_index[0] += 1
        except IndexError:
            card_index.append(1)
        total += card_index[0]
        winngNumbers, playerNumbers = parseLine(line)
        for playerNumber in playerNumbers.split():
            if playerNumber in winngNumbers.split():
                i += 1
                try:
                    card_index[i] += card_index[0] * 1
                except IndexError:
                    card_index.append(card_index[0] * 1)
        
        card_index.pop(0)


    print("Part 2: ", total)
    f.close()


def parseLine(line):
    split_game = line.split(":")
    number_split = split_game[1].split("|")
    winningNumbers = number_split[0]
    playerNumbers = number_split[1]


    return winningNumbers, playerNumbers

main()