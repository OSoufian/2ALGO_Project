from Box import Box
from greedy import box_stacking_g
from recursive import box_stacking_r

def refractor(file):
    boxes = open(f'{file}', 'r')
    Lines = boxes.readlines()
    box = [*map(lambda x: int(x), line.split())]
    boxList = []
    for line in Lines:
        boxList.append(Box(box[0], box[1], box[2]))
    return boxList

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
# box_stacking_r([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])
box_stacking_r(refractor("boxes.txt"))