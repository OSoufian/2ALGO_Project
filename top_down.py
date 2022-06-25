from Box import Box
from recursive import print_result

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
    H = [box.height for box in box_possibilities]
    max_height, max_stack = find_highest(box_possibilities, H, [], 1, track)
    print_result(max_height, max_stack)
    

def find_highest(boxes, H, max_stack, i, track):
    if track[i] > 0:
        return track[i]

    stacked_boxes = []
    for j in range(0, i):
        if boxes[i].width < boxes[j].width and boxes[i].depth < boxes[j].depth:
                if H[i] < H[j] + boxes[i].height:
                    H[i] = H[j] + boxes[i].height
                    stacked_boxes.append(boxes[j])    

    if i == (len(boxes) - 1):
        return max(H), stacked_boxes

    track[i] = H[i]

    return find_highest(boxes, H, max_stack, i+1)

box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])