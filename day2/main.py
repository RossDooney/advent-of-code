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

            red_new, green_new, blue_new = 0, 0, 0
            for x in re.finditer("red", segment):
                red_new = int(segment[x.start() - 3] + segment[x.start() - 2])
            for x in re.finditer("green", segment):
                green_new = int(segment[x.start() - 3] + segment[x.start() - 2])
            for x in re.finditer("blue", segment):
                blue_new = int(segment[x.start() - 3] + segment[x.start() - 2])

            if red_new > red:
                red = red_new
            if green_new > green:
                green = green_new
            if blue_new > blue:
                blue = blue_new

        total += red * blue * green
    
    print(total)   
        
main()