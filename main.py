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
        box = [*map(lambda x: int(x), line.split())]
        boxList.append(Box(box[0], box[1], box[2]))
        count += 1
    return boxList

sys.setrecursionlimit(2001)

# Algorithme glouton
# box_stacking_g([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_g(refractor("boxes.txt"))

#Algorithme récursive
# box_stacking_r([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_r(refractor("boxes.txt"))

#Algorithme top down
# box_stacking_tp([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_r(refractor("boxes.txt"))

#Algorithme bottom up
# box_stacking_bu([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_bu(refractor("boxes.txt"))