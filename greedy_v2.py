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
    max_stack = []

    n = len(box_possibilities)

    for i in range(1, n):
        stacked_boxes = []
        for j in range(0, i):
            if box_possibilities[i].width < box_possibilities[j].width and box_possibilities[i].depth < box_possibilities[j].depth:
                if max_height[i] < max_height[j] + box_possibilities[i].height:
                    max_height[i] = max_height[j] + box_possibilities[i].height
                    stacked_boxes.append(box_possibilities[j])
        if max_height[i] == max(max_height):
            max_stack = stacked_boxes

    print(max(max_height))
    
    for i in range(len(max_stack)):
        print(max_stack[i].height, 'x', max_stack[i].width, 'x', max_stack[i].depth)

box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])