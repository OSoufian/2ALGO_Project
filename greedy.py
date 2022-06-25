from Box import Box

def box_stacking_g(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, min(current_box.width, current_box.depth), max(current_box.width, current_box.depth))
        box_2 = Box(current_box.width, min(current_box.height, current_box.depth), max(current_box.height, current_box.depth))
        box_3 = Box(current_box.depth, min(current_box.width, current_box.height), max(current_box.width, current_box.height))
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)

    stacked_boxes = [box_possibilities[0]]

    for i in range(len(box_possibilities)):
        if box_possibilities[i].width < stacked_boxes[-1].width and box_possibilities[i].depth < stacked_boxes[-1].depth:
            stacked_boxes.append(box_possibilities[i])
    
    print_result(stacked_boxes)

def print_result(stacked_boxes):
    print("La hauteur maximale est :", sum(box.height for box in stacked_boxes))

    print("La répartition des boîtes est :")    
    for i in range(len(stacked_boxes)):
        print(stacked_boxes[i].height, 'x', stacked_boxes[i].width, 'x', stacked_boxes[i].depth)