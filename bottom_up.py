from typing_extensions import final
from Box import Box

def box_stacking(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, min(current_box.width, current_box.depth), max(current_box.width, current_box.depth))
        box_2 = Box(current_box.width, min(current_box.height, current_box.depth), max(current_box.height, current_box.depth))
        box_3 = Box(current_box.depth, min(current_box.width, current_box.height), max(current_box.width, current_box.height))
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)

    max_height = [box.height for box in box_possibilities]

    for i in range(1, len(box_possibilities)):
        stacked_boxes = []
        for j in range(0, i):
            if box_possibilities[i].width < box_possibilities[j].width and box_possibilities[i].depth < box_possibilities[j].depth:
                if max_height[i] < max_height[j] + box_possibilities[i].height:
                    max_height[i] = max_height[j] + box_possibilities[i].height
                    stacked_boxes.append(box_possibilities[j])
        stacked_boxes.append(box_possibilities[i])
        if max_height[i] == max(max_height):
            max_stack = stacked_boxes

    for _ in range(3):
        checkDoubles(max_stack)

    print(max(max_height))
    
    for i in range(len(max_stack)):
        print(max_stack[i].height, 'x', max_stack[i].width, 'x', max_stack[i].depth)

def refractor(file):
    boxes = open(f'{file}', 'r')
    Lines = boxes.readlines()
    boxList = []
    for line in Lines:
        boxList.append(Box([*map(lambda x: int(x), line.split())][0], [*map(lambda x: int(x), line.split())][1], [*map(lambda x: int(x), line.split())][2]))

    return boxList

def checkDoubles(max_stack):
    remove_stack = []
    for j in range(1, len(max_stack)-1):
        if (max_stack[j].width == max_stack[j+1].width and max_stack[j+1].depth < max_stack[j].depth) or (max_stack[j].depth == max_stack[j+1].depth and max_stack[j+1].width < max_stack[j].width) or (max_stack[j].width == max_stack[j+1].width and max_stack[j+1].depth == max_stack[j].depth):
            remove_stack.append(max_stack[j])
    for k in range(len(remove_stack)):
        max_stack.remove(remove_stack[k])
    return max_stack

box_stacking(refractor("boxes.txt"))