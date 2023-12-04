import os


f = open("input.txt", "r")

def main():
    total = 0
    for line in f:
        first = None
        last = None
        for char in line:
            if char.isnumeric():
                last = char
                if first is None:
                    first = char
        line_total = str(first) + str(last)
        total += int(line_total)
    print(total)

main()