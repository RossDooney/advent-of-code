import os
import re
import time



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
    
    index = searchLowestIndex(time, distance, round(time/2), 1)
    print(time - (2 * index) + 1)

def searchLowestIndex(time, dist, index, lowest):
    score = index * (time - index)
    lowest_check = (index-1) * (time - (index - 1))


    if dist < score and dist >= lowest_check:
        return index
    elif dist < score:
        new_index = round((index + lowest)/2)
        index = searchLowestIndex(time,dist,new_index,lowest)
        return index
    else:
        new_index = (index + (time/2))/2
        lowest = index
        
        index = searchLowestIndex(time,dist,new_index, lowest)

    return index




start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))