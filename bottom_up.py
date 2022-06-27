from Box import Box

def box_stacking_bu(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, min(current_box.width, current_box.depth), max(current_box.width, current_box.depth))
        box_2 = Box(current_box.width, min(current_box.height, current_box.depth), max(current_box.height, current_box.depth))
        box_3 = Box(current_box.depth, min(current_box.width, current_box.height), max(current_box.width, current_box.height))
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)

    H = [box.height for box in box_possibilities]

    for i in range(1, len(box_possibilities)):
        stacked_boxes = []
        for j in range(0, i):
            if box_possibilities[i].width < box_possibilities[j].width and box_possibilities[i].depth < box_possibilities[j].depth:
                if H[i] < H[j] + box_possibilities[i].height:
                    H[i] = H[j] + box_possibilities[i].height
                    stacked_boxes.append(box_possibilities[j])
        stacked_boxes.append(box_possibilities[i])
        if H[i] == max(H):
            max_stack = stacked_boxes

    for _ in range(3):
        checkDoubles(max_stack)

    # print(max(H))
    
    # for i in range(len(max_stack)):
    #     print(max_stack[i].height, 'x', max_stack[i].width, 'x', max_stack[i].depth)

    print_result(max(H), max_stack)

def checkDoubles(max_stack):
    remove_stack = []
    for j in range(1, len(max_stack)-1):
        if (max_stack[j].width == max_stack[j+1].width and max_stack[j+1].depth < max_stack[j].depth) or (max_stack[j].depth == max_stack[j+1].depth and max_stack[j+1].width < max_stack[j].width) or (max_stack[j].width == max_stack[j+1].width and max_stack[j+1].depth == max_stack[j].depth):
            remove_stack.append(max_stack[j])
    for k in range(len(remove_stack)):
        max_stack.remove(remove_stack[k])
    return max_stack

def print_result(max_height, stacked_boxes):
    print("La hauteur maximale est :", max_height)

    print("La répartition des boîtes est :")    
    for i in range(len(stacked_boxes)):
        print(stacked_boxes[i].height, 'x', stacked_boxes[i].width, 'x', stacked_boxes[i].depth)