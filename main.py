from Box import Box
from greedy import box_stacking_g
from recursive import box_stacking_r
from top_down import box_stacking_tp
from bottom_up import box_stacking_bu
import sys

def refractor(file):
    boxes = open(f'{file}', 'r')
    Lines = boxes.readlines()
    count = 0
    boxList = []
    for line in Lines:
        boxList.append(Box([*map(lambda x: int(x), line.split())][0], [*map(lambda x: int(x), line.split())][1], [*map(lambda x: int(x), line.split())][2]))
        count += 1
    return boxList

def refractor_v2(file):
    boxes = open(f'{file}', 'r')
    Lines = boxes.readlines()
    boxes = []
    for line in Lines:
        line = line.rstrip('\n')
        boxes.append(Box(*map(lambda x: int(x), line.split(','))))
    return boxes

sys.setrecursionlimit(2500)


# Algorithme glouton
# box_stacking_g([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_g(refractor("boxes.txt"))
# box_stacking_g(refractor_v2("boxes_2.txt"))

#Algorithme récursive
# box_stacking_r([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_r(refractor("boxes.txt"))

#Algorithme top down
# box_stacking_tp([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_r(refractor("boxes.txt"))

#Algorithme bottom up
# box_stacking_bu([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_bu(refractor("boxes.txt"))