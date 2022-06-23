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

    track = [0] * (len(box_possibilities) + 1)
    stacked_boxes = find_highest(box_possibilities, [], 0, track)
    print(sum(box.height for box in stacked_boxes))
    for i in range(len(stacked_boxes)):
        print(stacked_boxes[i].height, 'x', stacked_boxes[i].width, 'x', stacked_boxes[i].depth)

def find_highest(boxes, stacked_boxes, i, track):
    if stacked_boxes == []:
        stacked_boxes.append(boxes[i])

    elif track[i] > 0:
        return track[i]

    elif boxes[i].width < stacked_boxes[-1].width and boxes[i].depth < stacked_boxes[-1].depth:        
        stacked_boxes.append(boxes[i])

    if i == (len(boxes) - 1):
        return stacked_boxes
    
    track[i] = stacked_boxes

    return find_highest(boxes, stacked_boxes, i+1, track)

box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])