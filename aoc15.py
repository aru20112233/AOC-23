import pandas as pd
import numpy as np
aryan = pd.read_csv('inputday15.txt')
aryan = list(aryan)
aryan2 = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]
total=0
for j in range (0,len(aryan)):
    curr_value = 0
    for i in aryan[j]:
        if i=='.':
            break
        curr_value = ((curr_value+ord(i))*17)%256
    total=total+curr_value
print(curr_value)
print(total)

# value=0
# for i  in first:
#     if i=='.':
#         break
#     value = ((value+ord(i))*17)%256
# print(value)
import re
from collections import defaultdict

with open('inputday15.txt', 'r') as f:
    puzzle_input = f.read()


# def part1(puzzle_input):
#     total = 0
#     for step in puzzle_input.split(','):
#         current_val = 0
#         for char in step:
#             current_val += ord(char)
#             current_val *= 17
#             current_val %= 256
#         total += current_val

#     return total


def part2(puzzle_input):

    labels = defaultdict(list)
    lenses = defaultdict(list)
    regex = r'(\w+)(=|-)(\d+)?'
    for label, op, focal_len in re.findall(regex, puzzle_input):
        hash = 0
        for char in label:
            hash = (hash + ord(char)) * 17 % 256

        if label in labels[hash]:
            i = labels[hash].index(label)
            if op == '-':
                labels[hash].pop(i)
                lenses[hash].pop(i)
            else:
                lenses[hash][i] = int(focal_len)
        elif op == '=':
            labels[hash].append(label)
            lenses[hash].append(int(focal_len))

    total = 0
    for box, lenses in lenses.items():
        for i, focal_len in enumerate(lenses, start=1):
            total += (box+1) * i * focal_len
        
    return total


# print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))






