import os
import re


f = open("input.txt", "r")


def main():
    part1()


def part1():
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
    print(total)
            


def parseLine(line):
    split_game = line.split(":")
    number_split = split_game[1].split("|")
    winningNumbers = number_split[0]
    playerNumbers = number_split[1]


    return winningNumbers, playerNumbers

main()