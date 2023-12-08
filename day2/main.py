import os
import re


f = open("input.txt", "r")

def main():
    total = 0
    for line in f:
        red, green, blue = 0, 0, 0
        output_index = line.find(":")
        split_line = line[output_index+1:].split(";")
        for segment in split_line:
            
            if red > 12 or green > 13 or blue > 14:
                break
            red_new, green_new, blue_new = 0, 0, 0
            for x in re.finditer("red", segment):
                red_new = int(segment[x.start() - 3] + segment[x.start() - 2])
            for x in re.finditer("green", segment):
                green = int(segment[x.start() - 3] + segment[x.start() - 2])
            for x in re.finditer("blue", segment):
                blue = int(segment[x.start() - 3] + segment[x.start() - 2])

            if red_new > red:
                red = red_new
            if green_new > green:
                green = green_new
            if blue_new > blue:
                blue = blue_new
        print(red, green, blue)
        if red > 12 or green > 13 or blue > 14:
            continue
        print(line[5:output_index].strip())
        game_index = line[5:output_index].strip()
        total += int(game_index)
    print(total)


        



main()