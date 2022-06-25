from Box import Box
from greedy import box_stacking_g
from recursive import box_stacking_r

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

def print_result(stacked_boxes):
    print("La hauteur maximale est :", sum(box.height for box in stacked_boxes))

    print("La répartition des boîtes est :")    
    for i in range(len(stacked_boxes)):
        print(stacked_boxes[i].height, 'x', stacked_boxes[i].width, 'x', stacked_boxes[i].depth)


# Algorithme glouton
# box_stacking_g([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_g(refractor("boxes.txt"))
# box_stacking_g(refractor_v2("boxes_2.txt"))

#Algorithme récursive
box_stacking_r([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
# box_stacking_r(refractor("boxes.txt"))