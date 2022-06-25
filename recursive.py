from Box import Box

def box_stacking_r(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, min(current_box.width, current_box.depth), max(current_box.width, current_box.depth))
        box_2 = Box(current_box.width, min(current_box.height, current_box.depth), max(current_box.height, current_box.depth))
        box_3 = Box(current_box.depth, min(current_box.width, current_box.height), max(current_box.width, current_box.height))
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)    

    H = [box.height for box in box_possibilities]
    max_height, stacked_boxes = find_highest(box_possibilities, H, 1)
    print_result(max_height, stacked_boxes)

def find_highest(boxes, H, i):
    stacked_boxes = []
    for j in range(0, i):
        if boxes[i].width < boxes[j].width and boxes[i].depth < boxes[j].depth:
                if H[i] < H[j] + boxes[i].height:
                    H[i] = H[j] + boxes[i].height
                    stacked_boxes.append(boxes[j])

    if i == (len(boxes) - 1):
        return max(H), stacked_boxes

    return find_highest(boxes, H, i+1)

def print_result(max_height, stacked_boxes):
    print("La hauteur maximale est :", max_height)

    print("La répartition des boîtes est :")    
    for i in range(len(stacked_boxes)):
        print(stacked_boxes[i].height, 'x', stacked_boxes[i].width, 'x', stacked_boxes[i].depth)