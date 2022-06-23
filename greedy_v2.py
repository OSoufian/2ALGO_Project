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
    # stacked_boxes = []

    for i in range(1, len(box_possibilities)):
        for j in range(0, i):
            if box_possibilities[i].width < box_possibilities[j].width and box_possibilities[i].depth < box_possibilities[j].depth:
                if max_height[i] < max_height[j] + box_possibilities[i].height:
                    max_height[i] = max_height[j] + box_possibilities[i].height
                    # stacked_boxes[i].append(box_possibilities[i]) 

    print(max(max_height))
    
    # for i in range(len(stacked_boxes)):
    #     print(stacked_boxes[0][i].height, 'x', stacked_boxes[0][i].width, 'x', stacked_boxes[0][i].depth)

box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])