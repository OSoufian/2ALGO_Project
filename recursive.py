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

    stacked_boxes = find_highest(box_possibilities, [], 0)
    print(sum(box.height for box in stacked_boxes))

def find_highest(boxes, stacked_boxes, i):
    if stacked_boxes == []:
        stacked_boxes.append(boxes[i])

    elif boxes[i].width < stacked_boxes[-1].width and boxes[i].depth < stacked_boxes[-1].depth:
        if i == (len(boxes) - 1):
            return stacked_boxes
        stacked_boxes.append(boxes[i]) + find_highest(boxes, stacked_boxes, i+1)


box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])

# def box_stacking(boxes):
#     box_possibilities = []

#     for i in range(len(boxes)):
#         current_box = boxes[i]
#         box_possibilities += map(lambda a: Box(*a), it.permutations((current_box.height, current_box.width, current_box.depth)))

#     box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)    

#     stacked_boxes = find_highest(box_possibilities, [], 0)
#     print(sum(box.height for box in stacked_boxes))

# def find_highest(boxes, stacked_boxes, i):
#     if stacked_boxes == []:
#         stacked_boxes.append(boxes[i])

#     elif boxes[i].width < boxes[i+1].width and boxes[i].depth < boxes[i+1].depth:
#         if i == (len(boxes) - 1):
#             return stacked_boxes
#         stacked_boxes += [find_highest(boxes, stacked_boxes.append(boxes[i]), i+1)]


# box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])