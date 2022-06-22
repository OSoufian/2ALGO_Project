from Box import Box

def box_stacking(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, current_box.width, current_box.depth)
        box_2 = Box(current_box.depth, current_box.width, current_box.height)
        box_3 = Box(current_box.width, current_box.height, current_box.depth)
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)

    track = [0] * (len(box_possibilities))

    stacked_boxes = find_highest(box_possibilities, [], 0)
    print(sum(box.height for box in stacked_boxes))

def find_highest(boxes, stacked_boxes, i):
    if stacked_boxes == []:
        stacked_boxes.append(boxes[i])
        
    else:
        if boxes[i].width < stacked_boxes[-1].width and boxes[i].depth < stacked_boxes[-1].depth:
            stacked_boxes.append(boxes[i])

    if i == (len(boxes) - 1):
        return stacked_boxes

    return find_highest(boxes, stacked_boxes, i+1)


box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])