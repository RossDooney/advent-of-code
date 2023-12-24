import os
import re


def main():
    part1()
    part2()

def part1():
    f = open("input.txt", "r")
    inputTxt = f.readlines()
    time = re.sub("\s\s+" , " ", inputTxt[0].split(":")[1]).split(" ")
    distance = re.sub("\s\s+" , " ", inputTxt[1].split(":")[1]).split(" ")
    total = 1

    for x in range(1,len(time)):
        index = 0
        for y in range(int(time[x])):
            if int(distance[x]) < (y * (int(time[x])-y)):
                index =  int(time[x]) - (2 * y)  + 1
                break
          
                
        total *= index
    print(total)
    f.close()

def part2():
    f = open("input.txt", "r")
    inputTxt = f.readlines()
    time = int(''.join(re.sub("\s\s+" , " ", inputTxt[0].split(":")[1]).split(" ")))
    distance = int(''.join(re.sub("\s\s+" , " ", inputTxt[1].split(":")[1]).split(" ")))
    
    for x in range(time):
        if distance < (x * (time-x)):
            print(time - (2 * x) + 1)
            break

main()
