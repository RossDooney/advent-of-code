import os


f = open("input.txt", "r")
num_array = ["0", "zero", "1", "one", "2". "two", "3", "three", "4", "four", "5", "five"
             "6", "six", "7", "seven", "8", "eight", "9", "nine", "10", "ten"]

def main():
    total = 0
    for line in f:
        first = None
        last = None
        index = 0
        for num in num_array:
            if num in line:
                if first is None:
                    first = num
                

    print(total)

main()