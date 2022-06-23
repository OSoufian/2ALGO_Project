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

    max_heights = [box.height for box in box_possibilities]
    max_height = find_highest(box_possibilities, max_heights, 1)
    print(max_height)
    # print(sum(box.height for box in stacked_boxes))
    # for i in range(len(stacked_boxes)):
    #     print(stacked_boxes[i].height, 'x', stacked_boxes[i].width, 'x', stacked_boxes[i].depth)

def find_highest(boxes, max_heights, i):
    for j in range(0, i):
        if boxes[i].width < boxes[j].width and boxes[i].depth < boxes[j].depth:
                if max_heights[i] < max_heights[j] + boxes[i].height:
                    max_heights[i] = max_heights[j] + boxes[i].height

    if i == (len(boxes) - 1):
        return max(max_heights)

    return find_highest(boxes, max_heights, i+1)

box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])