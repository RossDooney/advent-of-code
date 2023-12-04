import os
import re


f = open("input.txt", "r")

def main():
    total = 0
    for line in f:
        red, green, blue = 0, 0, 0
        for x in re.finditer("red", line):
            red += int(line[x.start() - 3] + line[x.start() - 2])
        for x in re.finditer("green", line):
            green += int(line[x.start() - 3] + line[x.start() - 2])
        for x in re.finditer("blue", line):
            blue += int(line[x.start() - 3] + line[x.start() - 2])
        if red <= 12 and  green <= 13 and  blue <= 14:
            end_index = line.find(":")
            game_index = line[5:end_index].strip()
            total += int(game_index)
            print(game_index)
    print(total)


        



main()