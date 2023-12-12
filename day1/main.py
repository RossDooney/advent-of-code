import os


f = open("input.txt", "r")
num_list = ["1","2","3","4","5","6","7","8","9","one","two","three","four", "five", "six", "seven", "eight", "nine"]

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def main():
    total = 0
    number = 0
    for line in f:
        start_index = float("inf")
        start_word = ""
        end_index = float("-inf")
        end_word = ""
        for num in num_list:
            new_index = line.find(num)
            if new_index == -1:
                continue

            if  start_index > new_index:
                start_word = num
                start_index = new_index

            new_index = line.rfind(num)
            if end_index < new_index:
                end_word = num
                end_index = new_index
        

        start_word = convert_to_number(start_word)
        end_word = convert_to_number(end_word)
        number = start_word + end_word

  
        total += int(number)
    print(total)
        

            
def convert_to_number(num):
    try:
        return num_dict[num]
    except KeyError:
        return num


main()
